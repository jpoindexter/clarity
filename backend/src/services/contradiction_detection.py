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
                        "similarity_score": round(similarity, 3),
                        "contradiction_strength": contradiction_strength,
                        "contradiction_type": "semantic"
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
                        "similarity_score": round(boosted_similarity, 3),
                        "contradiction_strength": contradiction_strength,
                        "contradiction_type": "sentiment",
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
        "contradictions": contradictions,
        "financial_misinformation": financial_analysis,
        "metadata": {
            "processing_time": processing_time,
            "total_articles": len(articles),
            "total_contradictions": len(contradictions)
        }
    }
