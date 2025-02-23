def parse_feed(feed_data):
    """✅ Parses RSS feed data into structured articles."""
    articles = []
    source_name = feed_data.feed.get("title", "Unknown Source")  # ✅ Extract Source

    for entry in feed_data.entries:
        article = {
            "title": entry.get("title", "No Title"),
            "url": entry.get("link", "https://unknown.com"),  # ✅ Ensure URL exists
            "source": source_name,  # ✅ Include Source
            "published_at": entry.get(
                "published", "2025-02-21T00:00:00Z"
            ),  # ✅ Ensure Published Date
        }

        if "summary" in entry:
            article["summary"] = entry["summary"]

        articles.append(article)

    return articles
