# backend/src/utils/helpers.py

import re
import unicodedata


def clean_text(text):
    """Removes extra whitespace and normalizes text."""
    text = unicodedata.normalize("NFKD", text)
    return re.sub(r"\s+", " ", text).strip()


def generate_slug(title):
    """Creates a URL-friendly slug from a title."""
    title = clean_text(title)
    return re.sub(r"[^a-zA-Z0-9-]", "-", title).lower()


# Example usage:
# print(generate_slug("AI-Powered News Aggregator! 🚀")) -> "ai-powered-news-aggregator"
