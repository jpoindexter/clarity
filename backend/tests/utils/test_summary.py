import pytest
from backend.utils.summarizer import summarize_text

def test_summary_basic():
    """✅ Ensure text summarization works"""
    text = "AI is transforming industries."
    summary = summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) > 0

def test_summary_empty():
    """✅ Ensure empty input returns an error"""
    summary = summarize_text("")
    assert summary == "⚠️ Error: Input text is empty."

def test_summary_long_text():
    """✅ Ensure long text does not break"""
    text = "AI " * 100
    summary = summarize_text(text)
    assert len(summary) > 0