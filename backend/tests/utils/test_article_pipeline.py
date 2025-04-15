import pytest
from backend.utils.article_fetcher import fetch_article_text
from backend.utils.article_summarizer import summarize_article

def test_article_pipeline():
    """✅ End-to-end test: fetch and summarize a real article URL"""
    url = "https://example.com"
    text = fetch_article_text(url)
    assert isinstance(text, str) and len(text) > 0, "Failed to fetch article text"

    summary = summarize_article(text)
    assert isinstance(summary, str) and len(summary) > 0, "Failed to summarize article"