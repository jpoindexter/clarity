from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import torch
import os

# ✅ Fully disable MPS (Metal Performance Shaders) at execution level
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "0"
os.environ["PYTORCH_ENABLE_MPS"] = "0"
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Ensure no GPU execution

# ✅ Explicitly override MPS availability at runtime
torch.backends.mps.is_available = lambda: False
torch.backends.mps.is_built = lambda: False

# ✅ Enforce CPU execution and remove MPS tensors
torch.set_default_dtype(torch.float32)
torch.set_default_tensor_type(torch.FloatTensor)
torch.set_default_device("cpu")

# ✅ Log confirmation that MPS is disabled
print("🚀 System Check: MPS Availability:", torch.backends.mps.is_available())
print("🚀 System Check: MPS Built:", torch.backends.mps.is_built())
print("🚀 System Check: Using Device:", torch.device('cpu'))

# ✅ Use a more stable, lightweight model for contradiction detection
model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")

# ✅ Load FinBERT for financial misinformation detection
finbert = pipeline("text-classification", model="yiyanghkust/finbert-tone", device=-1)


def is_contradiction(text1, text2):
    """
    Uses sentence embeddings to determine if two texts contradict each other.
    """
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)

    similarity = util.pytorch_cos_sim(emb1, emb2).item()  # Cosine similarity

    # ✅ Improved logging for debugging
    print(
        f"Comparing: \"{text1[:50]}...\" <-> \"{text2[:50]}...\" | "
        f"Score: {similarity} | Threshold: 0.75"
    )

    return similarity < 0.75  # Threshold for contradiction detection


def analyze_financial_misinformation(text):
    """
    Uses FinBERT to determine whether a financial article is positive, negative,
    or neutral.
    """
    result = finbert(text)
    return result[0]  # Returns label and confidence score


def detect_contradictions(articles):
    """
    Uses NLP to detect contradictions between news articles.
    """
    contradictions = []
    financial_analysis = {}

    for i, article1 in enumerate(articles):
        for j, article2 in enumerate(articles):
            if i != j and is_contradiction(article1["content"], article2["content"]):
                contradictions.append((
                    article1["headline"],
                    article2["headline"]
                ))

        # ✅ Analyze financial misinformation using FinBERT
        financial_analysis[article1["headline"]] = analyze_financial_misinformation(
            article1["content"]
        )

    return {
        "contradictions": contradictions,
        "financial_misinformation": financial_analysis
    }
