from backend.src.database.db_connection import Base, SessionLocal, engine
from backend.src.models.article import Article

# Ensure all tables are created
Base.metadata.create_all(bind=engine)


def seed_database():
    """Seed the database with test articles."""
    db = SessionLocal()
    try:
        test_articles = [
            {
                "title": "Breaking News",
                "summary": "This is a test article about breaking news.",
                "content": "Breaking news content.",
                "source": "News",
                "url": "https://example.com/breaking-news",
            },
            {
                "title": "Tech Advances",
                "summary": "AI is revolutionizing the tech industry.",
                "content": "AI technology is evolving rapidly.",
                "source": "Tech",
                "url": "https://example.com/tech-advances",
            },
            {
                "title": "World Politics",
                "summary": "Geopolitical shifts are occurring worldwide.",
                "content": "The global political climate is changing.",
                "source": "Politics",
                "url": "https://example.com/world-politics",
            },
        ]

        for article in test_articles:
            existing = (
                db.query(Article).filter(Article.title == article["title"]).first()
            )
            if not existing:
                db.add(Article(**article))

        db.commit()
        print("✅ Database seeded successfully!")
    except Exception as e:
        db.rollback()
        print(f"❌ Database seeding failed: {e}")
    finally:
        db.close()
