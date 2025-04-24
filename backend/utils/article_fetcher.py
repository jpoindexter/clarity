

import feedparser

def fetch_articles(query: str):
    # Google News RSS URL
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    
    articles = []
    for entry in feed.entries:
        article = {
            "title": entry.title,
            "url": entry.link,
            "summary": entry.summary,
            "tone": "neutral",  # Placeholder, can be refined later
            "tags": ["general"],  # Placeholder tags
            "source": "Google News",
            "raw_text": entry.summary,
            "timestamp": entry.published,
            "manipulation_risk": 0.0  # Placeholder, to be added later
        }
        articles.append(article)
    
    return articles