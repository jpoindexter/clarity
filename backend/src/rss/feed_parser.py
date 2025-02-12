import feedparser

def fetch_rss_feed(feed_url):
    """
    Fetches RSS feed and returns parsed entries.
    """
    feed = feedparser.parse(feed_url)
    if not feed.entries:
        print(f"⚠️ No entries found for {feed_url}")
        return []
    return feed.entries

if __name__ == "__main__":
    test_url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    articles = fetch_rss_feed(test_url)
    for article in articles[:5]:  # Show first 5 articles for testing
        print(f"📰 {article.title} - {article.link}")
