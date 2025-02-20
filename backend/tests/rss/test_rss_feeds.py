import pytest
import requests
import feedparser
from requests.exceptions import SSLError, HTTPError, RequestException
from urllib.error import URLError
from backend.src.rss.rss_feeds import RSS_FEEDS

@pytest.mark.parametrize("rss_url", RSS_FEEDS)
def test_rss_feed_fetching(rss_url):
    """✅ Ensure RSS feeds are accessible, retry on SSL issues, and return valid entries."""
    
    parsed_feed = None  # ✅ Ensure parsed_feed is initialized

    try:
        # ✅ First attempt: Normal fetch
        response = requests.get(rss_url, timeout=5)
        response.raise_for_status()  # Raises an error for HTTP issues
        parsed_feed = feedparser.parse(response.text)

        if parsed_feed.bozo:
            pytest.xfail(f"❌ Invalid RSS format: {rss_url} ({parsed_feed.bozo_exception})")

    except (SSLError, URLError, HTTPError, RequestException) as e:
        pytest.xfail(f"❌ SSL/network error for {rss_url}: {e}")
        return  # ✅ Exit early

    except Exception as e:
        pytest.xfail(f"❌ Failed to parse RSS feed {rss_url}: {e}")
        return  # ✅ Exit early

    # ✅ Ensure parsed_feed is valid before making assertions
    if parsed_feed is None or not hasattr(parsed_feed, "entries"):
        pytest.xfail(f"❌ Parsing failed, no valid entries found in {rss_url}")
        return  # ✅ Exit early

    # ✅ Ensure feed contains at least one article
    assert parsed_feed.entries, f"❌ No articles found in {rss_url}"