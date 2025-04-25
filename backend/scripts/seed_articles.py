from datetime import datetime
import feedparser
from sqlalchemy.orm import Session
from backend.database.db_connection import SessionLocal
from backend.models.article import SummarizedArticle
from backend.schemas.schemas import SummarizedArticleCreate

def fetch_articles(query: str):
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    
    articles = []
    for entry in feed.entries:
        # Parse the timestamp using datetime.strptime
        timestamp = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S GMT")

        # Ensure 'tags' is a list
        tags = ["general"]  # Default tags

        article = {
            "title": entry.title,
            "url": entry.link,
            "summary": entry.summary,
            "tone": "neutral",  # Placeholder
            "tags": tags,  # Use list directly
            "source": "Google News",
            "raw_text": entry.summary,
            "timestamp": timestamp,
            "manipulation_risk": 0.0  # Placeholder
        }
        articles.append(article)
    
    return articles

def seed_database():
    db: Session = SessionLocal()

    # Fetch articles
    articles = fetch_articles("AI")

    for article in articles:
        # Check if article URL already exists
        existing_article = db.query(SummarizedArticle).filter(SummarizedArticle.url == article['url']).first()
        
        if existing_article:
            print(f"Skipping duplicate article: {article['title']}")
            continue  # Skip inserting duplicate articles

        # If not a duplicate, insert the article
        article_data = SummarizedArticleCreate(**article)
        db_article = SummarizedArticle(**article_data.dict())
        db.add(db_article)
    
    db.commit()
    db.refresh(db_article)
    db.close()

    print(f"✅ Seeded {len(articles)} articles into the database.")

if __name__ == "__main__":
    seed_database()