import logging

import feedparser
import requests

# ✅ Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ RSS Feed Sources
RSS_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://www.theguardian.com/world/rss",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://news.google.com/rss",
    "https://www.aljazeera.com/xml/rss/all.xml",
]


def fetch_rss_feed(url):
    """Fetch an RSS feed with SSL error handling."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # ✅ Raise error for HTTP issues
        parsed_feed = feedparser.parse(response.text)

        if parsed_feed.bozo:
            raise Exception(f"Invalid RSS format: {url}")

        feed_title = parsed_feed.feed.get("title", "Unknown Feed")
        logger.info(f"✅ Successfully fetched RSS feed: {feed_title} ({url})")
        return parsed_feed

    except requests.exceptions.SSLError:
        logger.warning(f"⚠️ SSL Error on {url}. Retrying without SSL verification...")
        try:
            response = requests.get(
                url, verify=False, timeout=5
            )  # ✅ Retry without SSL
            response.raise_for_status()
            parsed_feed = feedparser.parse(response.text)

            if parsed_feed.bozo:
                raise Exception(f"Invalid RSS format: {url}")

            feed_title = parsed_feed.feed.get("title", "Unknown Feed")
            logger.info(
                f"✅ Successfully fetched RSS feed (no SSL): {feed_title} ({url})"
            )
            return parsed_feed

        except Exception as e:
            logger.error(f"❌ Failed to fetch RSS feed {url}: {e}")
            return None  # ✅ Return None instead of crashing


def fetch_all_feeds():
    """Fetch all RSS feeds and return valid ones."""
    valid_feeds = []

    for url in RSS_FEEDS:
        parsed_feed = fetch_rss_feed(url)
        if parsed_feed:
            valid_feeds.append(parsed_feed)
        else:
            logger.error(f"❌ Skipping broken feed: {url}")

    logger.info(f"🔥 Successfully fetched {len(valid_feeds)} valid feeds.")
    return valid_feeds
