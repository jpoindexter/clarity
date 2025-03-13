import feedparser
import pytest

from backend.rss.feed_parser import parse_feed


# ✅ Mock RSS Feeds for Testing
@pytest.fixture
def mock_feed_valid():
    """✅ Provides a valid RSS feed structure."""
    return """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
        <channel>
            <title>Mock RSS Feed</title>
            <item>
                <title>Test Article</title>
                <link>https://example.com/test-article</link>
                <description>This is a test article summary.</description>
                <pubDate>Wed, 20 Feb 2025 12:00:00 GMT</pubDate>
            </item>
        </channel>
    </rss>
    """


@pytest.fixture
def mock_feed_missing_fields():
    """✅ Provides an RSS feed with missing fields to test robustness."""
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
def mock_feed_invalid():
    """✅ Provides an invalid RSS feed structure."""
    return """<html><body>This is not a valid RSS feed.</body></html>"""


# ✅ Tests
def test_parse_valid_feed(mock_feed_valid):
    """✅ Ensure valid RSS feeds are parsed correctly."""
    parsed_feed = feedparser.parse(mock_feed_valid)
    articles = parse_feed(parsed_feed)

    assert len(articles) == 1, "❌ Expected 1 article in the parsed feed."
    assert articles[0]["title"] == "Test Article", "❌ Title parsing failed."
    assert (
        articles[0]["url"] == "https://example.com/test-article"
    ), "❌ URL parsing failed."
    assert (
        articles[0]["summary"] == "This is a test article summary."
    ), "❌ Summary parsing failed."
    assert (
        articles[0]["published_at"] == "Wed, 20 Feb 2025 12:00:00 GMT"
    ), "❌ Published date parsing failed."


def test_parse_feed_missing_fields(mock_feed_missing_fields):
    """✅ Ensure missing fields don't break parsing."""
    parsed_feed = feedparser.parse(mock_feed_missing_fields)
    articles = parse_feed(parsed_feed)

    assert len(articles) == 1, "❌ Should still process articles with missing fields."
    assert (
        articles[0]["title"] == "Test Article"
    ), "❌ Title should be correctly parsed."
    assert (
        articles[0]["url"] == "https://example.com/test-article"
    ), "❌ URL should be correctly parsed."
    assert (
        "summary" not in articles[0] or articles[0]["summary"] is None
    ), "❌ Should not have summary if missing in feed."
    assert (
        "published_at" not in articles[0] or articles[0]["published_at"] is None
    ), "❌ Should not have published date if missing."


def test_parse_invalid_feed(mock_feed_invalid):
    """✅ Ensure invalid RSS feeds do not break parsing."""
    parsed_feed = feedparser.parse(mock_feed_invalid)
    articles = parse_feed(parsed_feed)

    assert len(articles) == 0, "❌ Invalid feed should not return any articles."
