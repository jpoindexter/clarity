"""
General Utility Helpers
Provides common helper functions for Clarity.
"""

import re
import unicodedata


def format_timestamp(timestamp):
    """
    Formats a timestamp into a readable string.
    """
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")


def clean_text(text: str) -> str:
    """
    Removes extra whitespace and normalizes text.

    Args:
        text (str): Input text to be cleaned.

    Returns:
        str: Cleaned text with normalized spaces.
    """
    text = unicodedata.normalize("NFKD", text)
    return re.sub(r"\s+", " ", text).strip()


def generate_slug(title: str) -> str:
    """
    Creates a URL-friendly slug from a title.

    Args:
        title (str): Input title to be converted into a slug.

    Returns:
        str: Slugified version of the title.
    """
    title = clean_text(title)
    return re.sub(r"[^a-zA-Z0-9-]", "-", title).lower()


# Example usage:
# print(generate_slug("AI-Powered News Aggregator! 🚀")) -> "ai-powered-news-aggregator"
