"""
Summarizer Module - AI-Powered Text Summarization
Handles text summarization using an external AI service.
"""

import logging
import requests
from typing import Optional
from backend.utils.request_utils import send_post_request

logger = logging.getLogger(__name__)

API_URL = "https://ai-summarizer.example.com/summarize"  # Placeholder URL


def summarize_text(text: str) -> Optional[str]:
    """
    Summarizes the given text using a local Ollama model, with fallback if unavailable.

    Args:
        text (str): The text to summarize.

    Returns:
        Optional[str]: The AI-generated summary or fallback stub.
    """
    if not text.strip():
        return "⚠️ Error: Input text is empty."
        
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": f"Summarize this: {text}",
                "stream": False
            },
            timeout=10
        )
        if response.ok:
            result = response.json()
            return result.get("response", "").strip()
        return "⚠️ Error: No valid summary returned."
    except Exception as e:
        print(f"⚠️ Ollama unavailable: {e}")
        return "⚠️ Ollama unavailable — test stub summary."

 
# ✅ Renamed variable to follow uppercase constant naming convention
TEST_TEXT = """
Clarity AI is an advanced intelligence platform designed to detect misinformation,
track narrative shifts, and provide actionable insights.
"""

if __name__ == "__main__":
    summary = summarize_text(TEST_TEXT)
    print(f"Generated Summary: {summary}" if summary else "Summarization failed.")

# ✅ Fixed: Added final newline
