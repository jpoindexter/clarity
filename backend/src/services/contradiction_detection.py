import spacy

# ✅ Load NLP model (small for efficiency)
nlp = spacy.load("en_core_web_sm")


def is_contradiction(text1, text2):
    """
    Uses NLP to determine if two texts contradict each other.
    If similarity is low, assume contradiction.
    """
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    similarity = doc1.similarity(doc2)  # Semantic similarity score (0-1)
    return similarity < 0.5  # If similarity is low, assume contradiction


def detect_contradictions(articles):
    """
    Uses NLP to detect contradictions between news articles.
    """
    contradictions = []
    for i, article1 in enumerate(articles):
        for j, article2 in enumerate(articles):
            if i != j and is_contradiction(article1["content"], article2["content"]):
                contradictions.append((article1["headline"], article2["headline"]))

    return contradictions
