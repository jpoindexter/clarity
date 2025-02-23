import sys

import feedparser

from backend.src.rss.rss_feeds import RSS_FEEDS
from backend.src.utils.summarizer import summarize_text

print("🔥 PYTHONPATH Debug:", sys.path)


def fetch_and_process_rss():
    """✅ Fetches RSS feeds, extracts articles, ensures required fields, and summarizes them safely."""
    articles = []
    MAX_ARTICLES = 5

    for rss_url in RSS_FEEDS:
        print(f"🔥 Fetching RSS Feed: {rss_url}")
        parsed_feed = feedparser.parse(rss_url)

        # DEBUG: Print raw feed output to see if it's working
        if not parsed_feed.entries:
            print(f"⚠️ WARNING: No entries found in {rss_url}")
            continue

        print(f"🔥 Raw Feed Data for {rss_url}: {parsed_feed.feed}")

        # Extract source name
        source_name = parsed_feed.feed.get("title", "Unknown Source")

        for entry in parsed_feed.entries:
            if len(articles) >= MAX_ARTICLES:
                break

            title = entry.get("title", "No Title")
            url = entry.get("link", "https://unknown.com")  # ✅ Ensure URL exists
            summary_source = entry.get("content", [{}])[0].get("value", title)
            published_at = entry.get(
                "published", "2025-02-21T00:00:00Z"
            )  # ✅ Ensure Published Date

            print(f"\n🔍 Fetching Article: {title}")
            print(f"🌐 URL: {url}")
            print(f"📰 Source: {source_name}")

            summary = (
                summarize_text(summary_source)
                if summary_source
                else "No summary available."
            )

            articles.append(
                {
                    "title": title,
                    "url": url,
                    "summary": summary,
                    "source": source_name,  # ✅ Include Source
                    "published_at": published_at,  # ✅ Include Published Date
                }
            )

            print(f"✅ Summary: {summary}")

        if len(articles) >= MAX_ARTICLES:
            break

    print(f"🚀 Fetching complete. Total articles fetched: {len(articles)}")
    print(f"📰 Sample article: {articles[0] if articles else 'No articles fetched'}")
    return articles


if __name__ == "__main__":
    fetch_and_process_rss()
