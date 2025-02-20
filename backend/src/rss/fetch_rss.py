import feedparser

from backend.src.rss.rss_feeds import RSS_FEEDS
from backend.src.utils.summarizer import summarize_text


def fetch_and_process_rss():
    """✅ Fetches RSS feeds, extracts articles, and summarizes them safely."""
    articles = []
    MAX_ARTICLES = 5

    for rss_url in RSS_FEEDS:
        parsed_feed = feedparser.parse(rss_url)

        if not hasattr(parsed_feed, "bozo") or parsed_feed.bozo:
            print(f"⚠️ Skipping {rss_url} due to parsing error.")
            continue

        for entry in parsed_feed.entries:
            if len(articles) >= MAX_ARTICLES:
                break

            title = entry.get("title", "No Title")
            url = entry.get("link")
            summary_source = entry.get("content", [{}])[0].get("value", title)

            print(f"\n🔍 Fetching Article: {title}")
            print(f"🌐 URL: {url}")

            summary = summarize_text(summary_source)

            articles.append(
                {
                    "title": title,
                    "url": url,
                    "summary": summary,
                }
            )

            print(f"✅ Summary: {summary}")

        if len(articles) >= MAX_ARTICLES:
            break

    print(f"🔥 DEBUG: Fetched {len(articles)} articles total.")
    return articles
