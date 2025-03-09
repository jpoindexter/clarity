from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import torch
import os
from functools import lru_cache

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


def detect_contradictions(articles):
    """
    Uses NLP to detect contradictions and financial misinformation.
    Processes all articles in batches for efficiency.
    """
    contradictions = []
    financial_analysis = {}

    # ✅ Batch encode all article content at once
    article_texts = [article["content"] for article in articles]
    embeddings = contradiction_model.encode(article_texts, convert_to_tensor=True)

    # ✅ Compare all embeddings efficiently
    for i, article1 in enumerate(articles):
        for j, article2 in enumerate(articles):
            if i != j:
                similarity = util.pytorch_cos_sim(embeddings[i], embeddings[j]).item()
                if similarity < 0.75:
                    contradictions.append({
                        "headline_1": article1["headline"],
                        "headline_2": article2["headline"],
                        "similarity_score": round(similarity, 3)
                    })
                    print(
                        f"Contradiction Found: {article1['headline']} <-> "
                        f"{article2['headline']} (Score: {similarity:.3f})"
                    )  # ✅ Improved logging

        # ✅ Use cached FinBERT analysis to speed up financial misinformation detection
        financial_analysis[article1["headline"]] = analyze_financial_misinformation(
            article1["content"]
        )

    return {
        "contradictions": contradictions,
        "financial_misinformation": financial_analysis
    }
