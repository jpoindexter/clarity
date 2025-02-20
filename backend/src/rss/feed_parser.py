def parse_feed(feed_data):
    """✅ Parses RSS feed data into structured articles."""
    articles = []
    for entry in feed_data.entries:
        article = {
            "title": entry.get("title", "No Title"),
            "url": entry.get("link"),
        }

        if "summary" in entry:
            article["summary"] = entry["summary"]
        if "published" in entry:
            article["published_at"] = entry["published"]

        articles.append(article)

    return articles
