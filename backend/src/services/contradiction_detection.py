from sentence_transformers import SentenceTransformer, util
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

# ✅ Use a more stable, lightweight model
model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")


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


def detect_contradictions(articles):
    """
    Uses NLP to detect contradictions between news articles.
    """
    contradictions = []
    for i, article1 in enumerate(articles):
        for j, article2 in enumerate(articles):
            if i != j and is_contradiction(
                article1["content"], article2["content"]
            ):
                contradictions.append((
                    article1["headline"],
                    article2["headline"]
                ))

    return contradictions
