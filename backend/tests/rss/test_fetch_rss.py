from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def mock_fetch_rss_feed():
    """✅ Mock `feedparser.parse()` & `summarize_text()` to return controlled test data."""
    mock_data = MagicMock()
    mock_data.bozo = 0  # ✅ Simulate successful RSS parse (No errors)
    mock_data.entries = [
        {
            "title": f"Test Article {i+1}",
            "link": f"https://example.com/test-article-{i+1}",
            "content": [{"value": f"Mocked Test Description {i+1}"}],
        }
        for i in range(5)
    ]

    with patch("feedparser.parse", return_value=mock_data):
        with patch(
            "backend.src.utils.summarizer.summarize_text", side_effect=lambda x: x
        ):  # ✅ Mock summarization
            yield mock_data


def test_fetch_rss_success(mock_fetch_rss_feed):
    """✅ Ensure RSS fetching works correctly with five mocked articles."""

    from backend.src.rss.fetch_rss import fetch_and_process_rss

    articles = fetch_and_process_rss()

    assert isinstance(articles, list), "❌ Expected a list of articles"
    assert len(articles) == 5, f"❌ Expected exactly 5 articles, got {len(articles)}"

    for i, article in enumerate(articles):
        expected_article = {
            "title": f"Test Article {i+1}",
            "url": f"https://example.com/test-article-{i+1}",
            "summary": f"Mocked Test Description {i+1}",  # ✅ Matches the mocked summary
        }
        assert (
            article == expected_article
        ), f"❌ Incorrect article data (Got: {article})"

    print(f"🔥 DEBUG: Test Passed - Fetched {len(articles)} articles correctly.")
