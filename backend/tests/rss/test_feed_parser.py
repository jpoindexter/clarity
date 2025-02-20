import pytest
import feedparser
from backend.src.rss.feed_parser import parse_feed

@pytest.fixture
def mock_valid_feed():
    """Mock a valid RSS feed response."""
    return """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
        <channel>
            <title>Mock RSS Feed</title>
            <item>
                <title>Test Article</title>
                <link>https://example.com/test-article</link>
                <description>This is a test summary.</description>
                <pubDate>Tue, 18 Feb 2025 12:34:56 GMT</pubDate>
            </item>
        </channel>
    </rss>
    """

@pytest.fixture
def mock_feed_missing_fields():
    """Mock an RSS feed with missing fields."""
    return """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
        <channel>
            <title>Mock RSS Feed</title>
            <item>
                <title>Test Article</title>
                <link>https://example.com/test-article</link>
            </item>
        </channel>
    </rss>
    """

@pytest.fixture
def mock_invalid_feed():
    """Mock an invalid/malformed RSS feed."""
    return """<rss><channel><title>Bad XML"""

def test_parse_valid_feed(mock_valid_feed):
    """✅ Ensure valid RSS feed is parsed correctly."""
    parsed_feed = feedparser.parse(mock_valid_feed)
    articles = parse_feed(parsed_feed)

    assert len(articles) == 1, "❌ Parsed feed should have one article."
    assert articles[0]['title'] == "Test Article", "❌ Incorrect article title."
    assert "summary" in articles[0], "❌ Missing article summary."
    assert "published_at" in articles[0], "❌ Missing published date."

def test_parse_feed_missing_fields(mock_feed_missing_fields):
    """✅ Ensure missing fields don't break parsing."""
    parsed_feed = feedparser.parse(mock_feed_missing_fields)
    articles = parse_feed(parsed_feed)

    assert len(articles) == 1, "❌ Should still process articles with missing fields."
    assert "summary" not in articles[0], "❌ Should not have summary if missing in feed."
    assert "published_at" not in articles[0], "❌ Should not have published date if missing."

def test_parse_invalid_feed(mock_invalid_feed):
    """✅ Ensure invalid RSS feed is handled gracefully."""
    parsed_feed = feedparser.parse(mock_invalid_feed)
    articles = parse_feed(parsed_feed)

    assert len(articles) == 0, "❌ Invalid feeds should return an empty list."