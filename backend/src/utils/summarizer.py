"""
Summarizer Module - AI-Powered Text Summarization
Handles text summarization using an external AI service.
"""

import json
import logging
from typing import Optional
import requests

logger = logging.getLogger(__name__)

API_URL = "https://ai-summarizer.example.com/summarize"  # Placeholder URL

def summarize_text(text: str) -> Optional[str]:
    """
    Summarizes the given text using an external AI API.

    Args:
        text (str): The text to summarize.

    Returns:
        Optional[str]: The AI-generated summary or None if an error occurs.
    """
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"text": text})

    try:
        response = requests.post(API_URL, data=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("summary")

    except requests.exceptions.Timeout as exc:
        logger.warning("Timeout error while summarizing text: %s", exc)
        return None

    except requests.exceptions.HTTPError as exc:
        logger.error("HTTP error while summarizing text: %s", exc)
        return None

    except requests.exceptions.RequestException as exc:
        logger.error("Network error occurred: %s", exc)
        return None


# ✅ Renamed variable to follow uppercase constant naming convention
TEST_TEXT = """
Clarity AI is an advanced intelligence platform designed to detect misinformation,
track narrative shifts, and provide actionable insights.
"""

if __name__ == "__main__":
    summary = summarize_text(TEST_TEXT)
    if summary:
        print(f"Generated Summary: {summary}")
    else:
        print("Summarization failed.")

# ✅ Fixed: Added final newline
