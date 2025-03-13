import logging
import json
import asyncio
import aiohttp
import feedparser

# ✅ Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Load RSS feeds from JSON file
<<<<<<< HEAD
RSS_FEED_FILE = "backend/src/rss/rss_sources.json"
=======
RSS_FEED_FILE = "backend/rss/rss_sources.json"
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917

try:
    with open(RSS_FEED_FILE, "r") as f:
        RSS_FEEDS = list(set(json.load(f)["feeds"]))  # ✅ Ensure unique feeds
except Exception as e:
    logger.error(f"❌ Failed to load RSS sources from {RSS_FEED_FILE}: {e}")
    RSS_FEEDS = []


async def fetch_rss_feed(url, session):
    """Asynchronously fetch an RSS feed with error handling."""
    try:
        async with session.get(url, timeout=5) as response:
            response.raise_for_status()
            content = await response.text()
            parsed_feed = feedparser.parse(content)

            if parsed_feed.bozo:
                raise Exception(f"Invalid RSS format: {url}")

            feed_title = parsed_feed.feed.get("title", "Unknown Feed")
            logger.info(f"✅ Successfully fetched RSS feed: {feed_title} ({url})")
            return parsed_feed

    except aiohttp.ClientError as e:
        logger.error(f"❌ Failed to fetch {url}: {e}")
        return None


async def fetch_all_feeds():
    """Asynchronously fetch all RSS feeds and return valid ones."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_rss_feed(url, session) for url in RSS_FEEDS]
        results = await asyncio.gather(*tasks)

    valid_feeds = [feed for feed in results if feed is not None]
    logger.info(f"🔥 Successfully fetched {len(valid_feeds)} valid feeds.")
    return valid_feeds


if __name__ == "__main__":
    asyncio.run(fetch_all_feeds())
