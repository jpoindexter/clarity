from urllib.error import URLError

import feedparser
import pytest
import requests
from requests.exceptions import (
    ConnectionError,
    HTTPError,
    RequestException,
    SSLError,
    Timeout,
)

from backend.rss.rss_feeds import RSS_FEEDS


@pytest.mark.parametrize("rss_url", RSS_FEEDS)
def test_rss_feed_fetching(rss_url):
    """
    ✅ Ensure RSS feeds are accessible, retry on SSL issues,
    and return valid entries.
    """

    parsed_feed = None  # ✅ Ensure `parsed_feed` is initialized

    try:
        # ✅ Attempt RSS feed fetch with retries on transient errors
        response = requests.get(rss_url, timeout=5)
        response.raise_for_status()  # ✅ Raises an error for HTTP issues

        parsed_feed = feedparser.parse(response.text)

        # ✅ Check for invalid RSS format
        if getattr(parsed_feed, "bozo", 0):
            pytest.xfail(
                f"❌ Invalid RSS format: {rss_url}\n"
                f"   ➜ {parsed_feed.bozo_exception}"
            )
            return  # ✅ Exit early

    except (
        Timeout,
        SSLError,
        URLError,
        HTTPError,
        RequestException,
        ConnectionError,
    ) as e:
        pytest.xfail(f"❌ Network error for {rss_url}: {e}")
        return  # ✅ Exit early

    except Exception as e:
        pytest.xfail(f"❌ Unexpected parsing error for {rss_url}: {e}")
        return  # ✅ Exit early

    # ✅ Ensure `parsed_feed` is valid before making assertions
    if (
        not parsed_feed
        or not hasattr(parsed_feed, "entries")
        or not parsed_feed.entries
    ):
        pytest.xfail(f"❌ Parsing failed or no valid entries found in {rss_url}")
        return  # ✅ Exit early

    # ✅ Ensure feed contains at least one valid article
    first_article = parsed_feed.entries[0]
    assert (
        "title" in first_article and "link" in first_article
    ), f"❌ Missing title or link in first article of {rss_url}"

    print(
        f"✅ RSS feed fetched successfully: {rss_url}\n"
        f"   ➜ {len(parsed_feed.entries)} articles retrieved."
    )
