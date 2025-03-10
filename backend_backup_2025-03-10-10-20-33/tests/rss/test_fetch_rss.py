from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def mock_fetch_rss_feed():
    """
    ✅ Mock `feedparser.parse()` & `summarize_text()`
    to return controlled test data.
    """
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
            "backend.src.utils.summarizer.summarize_text",
            side_effect=lambda x: x,  # ✅ Mock summarization
        ):
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
            "summary": f"Mocked Test Description {i+1}",  # ✅ Matches mock summary
        }
        assert (
            article == expected_article
        ), f"❌ Incorrect article data (Got: {article})"

    print(f"🔥 DEBUG: Test Passed - Fetched {len(articles)} articles correctly.")


@patch("feedparser.parse")
@patch("backend.src.utils.summarizer.summarize_text")
def test_fetch_rss_partial_entries(mock_summarize_text, mock_parse):
    """✅ Ensure it handles partial RSS entries."""
    mock_data = MagicMock()
    mock_data.bozo = 0
    mock_data.entries = [
        {
            "title": "Test Article 1",
            "link": "https://example.com/test-article-1",
            "content": [{"value": "Mocked Test Description 1"}],
        },
        {
            "title": "Test Article 2",
            "link": "https://example.com/test-article-2",
            # Missing content
        },
    ]
    mock_parse.return_value = mock_data

    from backend.src.rss.fetch_rss import fetch_and_process_rss

    articles = fetch_and_process_rss()

    assert isinstance(articles, list), "❌ Expected a list of articles"
    assert len(articles) == 1, f"❌ Expected 1 article, got {len(articles)}"

    expected_article = {
        "title": "Test Article 1",
        "url": "https://example.com/test-article-1",
        "summary": "Mocked Test Description 1",
    }
    assert articles[0] == expected_article, f"❌ Incorrect article data (Got: {articles[0]})"


@patch("feedparser.parse")
@patch("backend.src.utils.summarizer.summarize_text")
def test_fetch_rss_parse_error(mock_summarize_text, mock_parse):
    """✅ Ensure it handles RSS parse errors gracefully."""
    mock_data = MagicMock()
    mock_data.bozo = 1  # Simulate parse error
    mock_parse.return_value = mock_data

    from backend.src.rss.fetch_rss import fetch_and_process_rss

    articles = fetch_and_process_rss()

    assert isinstance(articles, list), "❌ Expected a list of articles"
    assert len(articles) == 0, f"❌ Expected 0 articles, got {len(articles)}"
