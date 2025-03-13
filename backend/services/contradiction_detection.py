<<<<<<< HEAD
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import torch
import os
from functools import lru_cache
import time

# ✅ Fully disable MPS (Metal Performance Shaders) for stability
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "0"
os.environ["PYTORCH_ENABLE_MPS"] = "0"
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# ✅ Explicitly override MPS detection
torch.backends.mps.is_available = lambda: False
torch.backends.mps.is_built = lambda: False
torch.set_default_device("cpu")

# ✅ Load contradiction detection model
contradiction_model = SentenceTransformer(
    "sentence-transformers/paraphrase-MiniLM-L6-v2"
)

# ✅ Load FinBERT for financial misinformation detection
finbert = pipeline("text-classification", model="yiyanghkust/finbert-tone", device=-1)


@lru_cache(maxsize=500)
def analyze_financial_misinformation(text):
    """
    Uses FinBERT to determine whether a financial article is positive, negative,
    or neutral.
    Implements caching to avoid redundant analysis.
    """
    result = finbert(text)
    analysis = {
        "label": result[0]["label"],
        "score": round(result[0]["score"], 3)  # Rounded for cleaner output
    }
    print(f"FinBERT Analysis: {analysis}")  # ✅ Improved logging
    return analysis


def detect_contradictions(articles, min_similarity_threshold=0.5):
    """
    Uses NLP to detect contradictions and financial misinformation.
    Processes all articles in batches for efficiency.
    Allows filtering contradictions by minimum similarity threshold.
    Now includes sentiment-based contradiction detection.
    """
    start_time = time.time()
    contradictions = []
    financial_analysis = {}

    # ✅ Batch encode all article content at once
    article_texts = [article["content"] for article in articles]
    embeddings = contradiction_model.encode(article_texts, convert_to_tensor=True)

    # ✅ Compute FinBERT sentiment analysis for each article
    for article in articles:
        financial_analysis[article["headline"]] = analyze_financial_misinformation(
            article["content"]
        )

    # ✅ Compare all embeddings efficiently
    for i, article1 in enumerate(articles):
        for j, article2 in enumerate(articles):
            if i != j:
                similarity = util.pytorch_cos_sim(embeddings[i], embeddings[j]).item()

                # ✅ Log all similarity scores for debugging
                print(
                    f"Checking: {article1['headline']} <-> {article2['headline']} "
                    f"(Similarity: {similarity:.3f})"
                )

                # ✅ Contradiction detection by similarity (Lowered threshold to 0.55)
                if similarity < 0.55 and similarity >= min_similarity_threshold:
                    # Higher strength = stronger contradiction
                    contradiction_strength = round(1 - similarity, 3)
                    contradictions.append({
                        "headline_1": article1["headline"],
                        "headline_2": article2["headline"],
                        "score": round(similarity, 3),
                        "strength": contradiction_strength,
                        "type": "semantic"
                    })
                    print(
                        f"Contradiction Found (Semantic): {article1['headline']} <-> "
                        f"{article2['headline']} (Score: {similarity:.3f}, "
                        f"Strength: {contradiction_strength:.3f})"
                    )

                # ✅ Contradiction detection by sentiment
                sentiment1 = financial_analysis[article1["headline"]]["label"]
                sentiment2 = financial_analysis[article2["headline"]]["label"]

                if (sentiment1 == "Positive" and sentiment2 == "Negative") or \
                   (sentiment1 == "Negative" and sentiment2 == "Positive"):
                    # ✅ Boost contradiction confidence if similarity is
                    # borderline (0.5+)
                    boosted_similarity = max(similarity, 0.55)
                    # Sentiment-based contradictions are considered strong
                    contradiction_strength = 0.9

                    contradictions.append({
                        "headline_1": article1["headline"],
                        "headline_2": article2["headline"],
                        "score": round(boosted_similarity, 3),
                        "strength": contradiction_strength,
                        "type": "sentiment",
                        "sentiment_1": sentiment1,
                        "sentiment_2": sentiment2
                    })
                    print(
                        f"Contradiction Found (Sentiment): {article1['headline']} "
                        f"({sentiment1}) <-> {article2['headline']} ({sentiment2})"
                        f" - Boosted Similarity: {boosted_similarity:.3f}, "
                        f"Strength: {contradiction_strength:.3f}"
                    )

    processing_time = round(time.time() - start_time, 3)

    return {
=======
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
    return SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")


def get_finbert():
    return pipeline("text-classification", model="yiyanghkust/finbert-tone")


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


@router.post("/api/contradictions/detect")
async def detect_contradictions(
    request: Request,
    contradiction_model: SentenceTransformer = Depends(get_contradiction_model),
    finbert: pipeline = Depends(get_finbert),
):
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

    start_time = time.time()
    financial_analysis = {}
    article_texts = [article.content for article in articles]

    try:
        embeddings = await asyncio.to_thread(
            contradiction_model.encode, article_texts, convert_to_tensor=True
        )
    except Exception as e:
        logger.error(f"Embedding error: {e}")
        raise HTTPException(
            status_code=500,
            detail={"error": "Internal Server Error", "message": str(e)},
        )

    try:
        for article in articles:
            financial_analysis[article.headline] = (
                await analyze_financial_misinformation(article.content, finbert)
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
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
        "contradictions": contradictions,
        "financial_misinformation": financial_analysis,
        "metadata": {
            "processing_time": processing_time,
            "articles_analyzed": len(articles),
            "total_contradictions": len(contradictions)
        }
    }
<<<<<<< HEAD
=======
    logger.debug(f"Final API response: {response}")
    return response
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
