import feedparser
from datetime import datetime
from backend.src.database.db_connection import SessionLocal
from backend.src.models.article import Article

"""
RSS Feed Ingestion & Parsing.
"""

RSS_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://www.theguardian.com/world/rss",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.cnn.com/rss/edition.rss",
    "https://news.google.com/rss"
]

def fetch_rss_articles():
    """Fetch and parse articles from RSS feeds."""
    session = SessionLocal()
    articles_added = 0
    
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        
        for entry in feed.entries:
            existing_article = session.query(Article).filter_by(title=entry.title).first()
            
            if not existing_article:
                new_article = Article(
                    title=entry.title,
                    summary=entry.summary if hasattr(entry, 'summary') else "",
                    content=entry.content[0].value if hasattr(entry, 'content') else "",
                    source=feed.feed.title,
                    url=entry.link,
                    published_at=datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else datetime.utcnow()
                )
                session.add(new_article)
                articles_added += 1
    
    session.commit()
    session.close()
    print(f"✅ Fetched & Stored {articles_added} new articles from RSS feeds.")

if __name__ == "__main__":
    fetch_rss_articles()
