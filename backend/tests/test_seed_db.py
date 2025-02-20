from backend.src.database.db_connection import SessionLocal
from backend.src.database.seed_db import seed_database
from backend.src.models.article import Article


def test_seed_database():
    """Test seeding the database with test articles."""
    # Run the seed function
    seed_database()

    db = SessionLocal()
    try:
        # Check if articles exist
        articles = db.query(Article).all()
        assert len(articles) > 0, "❌ Seeding failed, no articles found"
    finally:
        db.close()
