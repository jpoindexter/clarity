import pytest
from backend.utils.summary_generator import summarize_text
from unittest.mock import patch
import requests

def test_summarize_text_success():
    """✅ Ensure summarize_text returns actual summary from Ollama"""
    summary = summarize_text("AI is the future.")
    assert isinstance(summary, str)
    assert len(summary) > 10

def test_summarize_text_empty():
    """✅ Ensure it handles empty input properly."""
    summary = summarize_text("")
    assert summary == "⚠️ Error: Input text is empty."

def test_summarize_text_none():
    """✅ Ensure it handles None input gracefully."""
    summary = summarize_text(None)
    assert summary == "⚠️ Error: Input text is empty."

def test_summarize_text_error_unavailable():
    """✅ Simulate Ollama error by mocking requests.post to raise exception."""
    with patch("backend.utils.summary_generator.requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.ConnectionError("Simulated Ollama failure")
        result = summarize_text("Trigger fallback.")
        assert "⚠️ Error: Ollama service unavailable" in result