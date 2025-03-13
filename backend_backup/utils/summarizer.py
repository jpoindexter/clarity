"""
Summarizer Module - AI-Powered Text Summarization
Handles text summarization using an external AI service.
"""

import logging
from typing import Optional
from backend.utils.request_utils import send_post_request

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
    response = send_post_request(API_URL, text)
    return response.get("summary") if response else None


# ✅ Renamed variable to follow uppercase constant naming convention
TEST_TEXT = """
Clarity AI is an advanced intelligence platform designed to detect misinformation,
track narrative shifts, and provide actionable insights.
"""

if __name__ == "__main__":
    summary = summarize_text(TEST_TEXT)
    print(f"Generated Summary: {summary}" if summary else "Summarization failed.")

# ✅ Fixed: Added final newline
