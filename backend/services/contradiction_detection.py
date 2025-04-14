import time
import logging
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, HTTPException, Request, Depends
import asyncio

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter() 


def get_contradiction_model():
    try:
        logger.info("🚀 Loading contradiction model...")
        model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")
        logger.info("✅ Contradiction model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"❌ Failed to load contradiction model: {e}")
        raise RuntimeError("Failed to initialize contradiction model")


def get_finbert():
    try:
        logger.info("🚀 Loading FinBERT model for sentiment analysis...")
        model = pipeline("text-classification", model="yiyanghkust/finbert-tone")
        logger.info("✅ FinBERT model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"❌ Failed to load FinBERT model: {e}")
        raise RuntimeError("Failed to initialize FinBERT")


class Article(BaseModel):
    source: str
    headline: str
    content: str
    sentiment_1: Optional[float] = None
    sentiment_2: Optional[float] = None
    contradiction_score: Optional[float] = None


async def analyze_financial_misinformation(text: str, finbert):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, lambda: finbert(text))
    return result[0]


async def calculate_contradictions(articles, embeddings, financial_analysis):
    contradictions = []
    for i, article1 in enumerate(articles):
        for j, article2 in enumerate(articles):
            if i >= j:
                continue
            similarity = util.pytorch_cos_sim(embeddings[i], embeddings[j]).item()
            if 0.5 <= similarity < 0.55:
                contradictions.append({
                    "headline_1": article1.headline,
                    "headline_2": article2.headline,
                    "score": round(similarity, 3),
                    "strength": round(1 - similarity, 3),
                    "type": "semantic"
                })
            sentiment1 = financial_analysis[article1.headline]["label"]
            sentiment2 = financial_analysis[article2.headline]["label"]
            if {sentiment1, sentiment2} == {"Positive", "Negative"}:
                contradictions.append({
                    "headline_1": article1.headline,
                    "headline_2": article2.headline,
                    "score": round(max(similarity, 0.55), 3),
                    "strength": 0.9,
                    "type": "sentiment",
                    "sentiment_1": sentiment1,
                    "sentiment_2": sentiment2
                })
    return contradictions


@router.post("/contradictions/detect")
async def detect_contradictions(
    request: Request,
    contradiction_model: SentenceTransformer = Depends(get_contradiction_model),
    finbert: pipeline = Depends(get_finbert),
):
    logger.info("🚀 Starting contradiction detection process")
    start_time = time.time()
    try:
        body = await request.json()
        if not isinstance(body, dict) or "articles" not in body or not isinstance(
            body["articles"], list
        ):
            raise HTTPException(status_code=400, detail="Invalid request format")
        articles = [Article(**article) for article in body["articles"]]
    except Exception as e:
        logger.error(f"Request parsing failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    financial_analysis = {}
    article_texts = [article.content for article in articles]

    try:
        logger.info("🚀 Generating embeddings for articles...")
        embeddings = await asyncio.to_thread(
            contradiction_model.encode, article_texts, convert_to_tensor=True
        )
        logger.info("✅ Embeddings generated successfully")
    except Exception as e:
        logger.error(f"❌ Embedding error: {e}")
        raise HTTPException(
            status_code=500,
            detail={"error": "Internal Server Error", "message": str(e)},
        )

    try:
        for article in articles:
            logger.info(f"🧠 Analyzing sentiment for article: {article.headline}")
            financial_analysis[article.headline] = (
                await analyze_financial_misinformation(article.content, finbert)
            )
            logger.info(
                f"✅ Sentiment analysis result: {financial_analysis[article.headline]}"
            )
    except Exception as e:
        logger.error(f"Sentiment analysis failed: {e}")
        raise HTTPException(
            status_code=500,
            detail={"error": "Sentiment analysis error", "message": str(e)}
        )

    contradictions = await calculate_contradictions(
        articles, embeddings, financial_analysis
    )

    processing_time = round(time.time() - start_time, 3)
    response = {
        "contradictions": contradictions,
        "financial_misinformation": financial_analysis,
        "metadata": {
            "processing_time": processing_time,
            "articles_analyzed": len(articles),
            "total_contradictions": len(contradictions)
        }
    }
    logger.debug(f"Final API response: {response}")
    return response
