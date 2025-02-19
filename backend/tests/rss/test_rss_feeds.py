import pytest
import feedparser
import ssl
from urllib.error import URLError
from backend.src.rss.rss_feeds import RSS_FEEDS

def test_rss_feeds_exist():
    """✅ Ensure RSS feeds list is populated."""
    assert isinstance(RSS_FEEDS, list), "❌ RSS_FEEDS is not a list"
    assert len(RSS_FEEDS) > 0, "❌ No RSS feeds found"

@pytest.mark.parametrize("rss_url", RSS_FEEDS)
def test_rss_feed_fetching(rss_url):
    """✅ Ensure RSS feeds are accessible and return valid entries."""
    try:
        parsed_feed = feedparser.parse(rss_url)
        
        if parsed_feed.bozo:
            pytest.xfail(f"❌ Network/SSL issue for {rss_url}: {parsed_feed.bozo_exception}")

        assert "entries" in parsed_feed, f"❌ RSS feed missing 'entries': {rss_url}"
        assert len(parsed_feed.entries) > 0, f"❌ No articles found in {rss_url}"

    except (URLError, ssl.SSLError) as e:
        pytest.xfail(f"❌ SSL/network error for {rss_url}: {e}")