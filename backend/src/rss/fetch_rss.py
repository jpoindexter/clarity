import feedparser
import time
from backend.src.rss.rss_feeds import RSS_FEEDS
from backend.src.utils.summarizer import summarize_text

def fetch_and_process_rss():
    """✅ Fetches RSS feeds, extracts articles, and summarizes them safely."""
    articles = []

    for rss_url in RSS_FEEDS:
        parsed_feed = feedparser.parse(rss_url)

        if parsed_feed.bozo:
            print(f"⚠️ Skipping {rss_url} due to parsing error: {parsed_feed.bozo_exception}")
            continue

        for entry in parsed_feed.entries[:5]:  # ✅ Limit to first 5 to prevent infinite loops
            title = entry.get("title", "No Title")
            url = entry.get("link", None)
            summary_source = entry.get("content", [{}])[0].get("value", title)

            # ✅ Debug before summarization
            print(f"\n🔍 Fetching Article: {title}")
            print(f"🌐 URL: {url}")

            # ✅ Limit API calls with a rate limit
            time.sleep(1.5)  # 🕒 Prevents hitting API too fast

            summary = summarize_text(summary_source)

            articles.append({
                "title": title,
                "url": url,
                "summary": summary,
            })

            # ✅ Debug after summarization
            print(f"✅ Summary: {summary}")

    return articles


if __name__ == "__main__":
    processed_articles = fetch_and_process_rss()

    print("\n✅ **Final Articles** ✅")
    for article in processed_articles:
        print(f"\n🔹 {article['title']}\n🔗 {article['url']}\n📝 {article['summary']}")