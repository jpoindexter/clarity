import json
import requests
from typing import Dict, Any

def detect_bias(text: str) -> Dict[str, Any]:
    """Detects bias in a given article."""
    # ... (rest of the function remains unchanged)

def score_credibility(text: str) -> Dict[str, Any]:
    """Scores the credibility of a news article."""
    # ... (rest of the function remains unchanged)

def find_contradictions(article_text: str, related_text: str) -> Dict[str, Any]:
    """Compares two articles to detect contradictions."""
    # ... (rest of the function remains unchanged)

def track_media_influence(text: str) -> Dict[str, Any]:
    """Tracks how a news article spreads through different media sources."""
    # ... (rest of the function remains unchanged)

def fact_check_article(text: str) -> Dict[str, Any]:
    """Performs basic fact-checking on an article using an AI-powered approach."""
    # ... (rest of the function remains unchanged)

def detect_misinformation(text: str) -> Dict[str, Any]:
    """Detects misinformation in the given text using AI-powered analysis."""
    if not text.strip():
        return {"error": "Text is empty."}

    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={"model": "mistral", "prompt": f"Detect misinformation: {text}"},
        )
        response.raise_for_status()

        data = response.json()
        return {
            "misinformation_score": data.get("misinformation_score", "N/A"),
            "false_claims": data.get("false_claims", "No false claims detected.")
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"AI service unavailable. Details: {e}"}
