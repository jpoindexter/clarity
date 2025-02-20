import feedparser
import time
from backend.src.rss.rss_feeds import RSS_FEEDS
from backend.src.utils.summarizer import summarize_text  # ✅ Moved outside to prevent circular imports

def fetch_and_process_rss():
    """✅ Fetches RSS feeds, extracts articles, and summarizes them safely."""
    articles = []
    MAX_ARTICLES = 5  # ✅ Hard limit on the number of articles TOTAL

    for rss_url in RSS_FEEDS:
        parsed_feed = feedparser.parse(rss_url)

        # ✅ Ensure parsed_feed is valid and check for `bozo` safely
        if not hasattr(parsed_feed, "bozo") or parsed_feed.bozo:
            print(f"⚠️ Skipping {rss_url} due to parsing error.")
            continue

        for entry in parsed_feed.entries:
            if len(articles) >= MAX_ARTICLES:  # ✅ Stop collecting after 5 articles TOTAL
                break

            title = entry.get("title", "No Title")
            url = entry.get("link", None)
            summary_source = entry.get("content", [{}])[0].get("value", title)

            print(f"\n🔍 Fetching Article: {title}")
            print(f"🌐 URL: {url}")

            summary = summarize_text(summary_source)

            articles.append({
                "title": title,
                "url": url,
                "summary": summary,
            })

            print(f"✅ Summary: {summary}")

        if len(articles) >= MAX_ARTICLES:
            break  # ✅ Stop processing feeds if we've hit the limit

    print(f"🔥 DEBUG: Fetched {len(articles)} articles total.")  # ✅ Debugging
    return articles