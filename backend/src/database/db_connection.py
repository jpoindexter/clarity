import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://jpoindexter:dontforgetme@localhost:5432/clarity")

# ✅ Ensure database URL is set
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set. Check your environment variables.")

# ✅ Create database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Define Base model
Base = declarative_base()

# ✅ Dependency for DB session
def get_db():
    """Create a new database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Function to fetch RSS feeds from DB
def get_rss_feeds():
    """Fetch RSS feeds from the database (placeholder, replace with actual query)."""
    try:
        with SessionLocal() as db:
            # Replace with actual SQLAlchemy query (example: db.query(RSSFeed).all())
            return []  # Return empty list as fallback
    except Exception as e:
        print(f"⚠️ Database error in get_rss_feeds: {e}")
        return []  # Ensure function returns something even if DB fails
