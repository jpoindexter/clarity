import json
from unittest.mock import patch
import pytest
from backend.src.utils.summarizer import summarize_text


@pytest.fixture
def mock_ollama_response():
    """Mock the Ollama API response."""
    return json.dumps({"response": "AI is transforming the world."})


@patch("requests.post")
def test_summarize_text_success(mock_post, mock_ollama_response):
    """✅ Ensure summarize_text returns expected summary"""
    mock_post.return_value.status_code = 200
    mock_post.return_value.iter_lines.return_value = [mock_ollama_response.encode()]

    summary = summarize_text("AI is the future.")
    assert summary == "AI is transforming the world."


@patch("requests.post")
def test_summarize_text_empty(mock_post):
    """✅ Ensure it handles empty input properly."""
    summary = summarize_text("")
    assert summary == "⚠️ Error: Input text is empty."


@patch("requests.post")
def test_summarize_text_error(mock_post):
    """✅ Ensure it handles API errors gracefully."""
    mock_post.return_value.status_code = 500  # ✅ Mock API failure
    mock_post.return_value.json.return_value = {"error": "Server Down"}

    summary = summarize_text("AI is powerful.")
    assert "⚠️ Error: Ollama service unavailable" in summary


@patch("requests.post")
def test_summarize_text_partial_response(mock_post):
    """✅ Ensure it handles partial API responses."""
    partial_response = json.dumps({"response": "AI is"})
    mock_post.return_value.status_code = 200
    mock_post.return_value.iter_lines.return_value = [partial_response.encode()]

    summary = summarize_text("AI is the future.")
    assert summary == "AI is"


@patch("requests.post")
def test_summarize_text_invalid_json(mock_post):
    """✅ Ensure it handles invalid JSON responses."""
    invalid_json_response = "Invalid JSON"
    mock_post.return_value.status_code = 200
    mock_post.return_value.iter_lines.return_value = [invalid_json_response.encode()]

    summary = summarize_text("AI is the future.")
    assert "⚠️ Error: Invalid response from Ollama" in summary