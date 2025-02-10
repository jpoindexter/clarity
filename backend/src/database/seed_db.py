from backend.src.database.db_connection import SessionLocal, engine, Base
from backend.src.database.models.article import Article

# Ensure all tables are created
Base.metadata.create_all(bind=engine)

def seed_database():
    """Seed the database with test articles."""
    db = SessionLocal()

    test_articles = [
        {"title": "Breaking News", "summary": "This is a test article about breaking news.", "source": "News"},
        {"title": "Tech Advances", "summary": "AI is revolutionizing the tech industry.", "source": "Tech"},
        {"title": "World Politics", "summary": "Geopolitical shifts are occurring worldwide.", "source": "Politics"}
    ]

    for article in test_articles:
        existing = db.query(Article).filter(Article.title == article["title"]).first()
        if not existing:
            new_article = Article(**article)
            db.add(new_article)

    db.commit()
    db.close()
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
