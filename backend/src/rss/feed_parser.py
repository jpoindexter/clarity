def parse_feed(feed_data):
    """
    ✅ Parses RSS feed data into structured articles, ensuring deduplication
    & handling errors.
    """
    articles = []
    seen_urls = set()  # ✅ Track processed URLs to prevent duplicates
    source_name = feed_data.feed.get("title", "Unknown Source")  # ✅ Extract Source

    for entry in feed_data.entries:
        try:
            url = entry.get("link", "https://unknown.com")

            # ✅ Deduplication: Skip if URL already processed
            if url in seen_urls:
                continue
            seen_urls.add(url)

            article = {
                "title": entry.get("title", "No Title"),
                "url": url,
                "source": source_name,  # ✅ Include Source
                "published_at": entry.get("published", "2025-02-21T00:00:00Z"),
            }

            # ✅ Ensure summary exists & is long enough for processing
            if "summary" in entry:
                summary = entry["summary"]
                if len(summary.split()) > 100:  # ✅ Only process long summaries
                    article["summary"] = summary

            articles.append(article)

        except Exception as e:
            print(f"❌ Error processing entry from {source_name}: {e}")

    return articles
