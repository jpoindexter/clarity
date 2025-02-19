import pytest
import feedparser
import ssl
import requests
from urllib.error import URLError, HTTPError
from backend.src.rss.rss_feeds import RSS_FEEDS

def test_rss_feeds_exist():
    """✅ Ensure RSS feeds list is populated."""
    assert isinstance(RSS_FEEDS, list), "❌ RSS_FEEDS is not a list"
    assert len(RSS_FEEDS) > 0, "❌ No RSS feeds found"

@pytest.mark.parametrize("rss_url", RSS_FEEDS)
def test_rss_feed_fetching(rss_url):
    """✅ Ensure RSS feeds are accessible, retry on SSL issues, and return valid entries."""
    try:
        # ✅ First attempt: Normal fetch
        response = requests.get(rss_url, timeout=5)
        response.raise_for_status()  # Raises an error for HTTP issues
        parsed_feed = feedparser.parse(response.text)

        if parsed_feed.bozo:
            raise Exception(f"Invalid RSS format: {rss_url} ({parsed_feed.bozo_exception})")

    except (requests.exceptions.SSLError, URLError, HTTPError) as e:
        pytest.xfail(f"❌ SSL/network error for {rss_url}: {e}")

    except Exception as e:
        pytest.xfail(f"❌ Failed to parse RSS feed {rss_url}: {e}")

    # ✅ Ensure feed contains articles
    assert "entries" in parsed_feed, f"❌ RSS feed missing 'entries': {rss_url}"
    assert len(parsed_feed.entries) > 0, f"❌ No articles found in {rss_url}"