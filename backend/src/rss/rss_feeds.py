"""
RSS Feed Configuration.

Handles fetching RSS feeds from the database and provides a default fallback list.
"""

from sqlalchemy.exc import SQLAlchemyError  # ✅ Import specific exception
from ..database.db_connection import get_rss_feeds  # ✅ Ensure function exists before importing

def fetch_rss_feeds():
    """Fetch the latest RSS feeds from the database."""
    try:
        feeds = get_rss_feeds()  # ✅ Fetch feeds from DB
        if not feeds:
            raise ValueError("No feeds found in DB. Falling back to default list.")
        return feeds
    except SQLAlchemyError as e:  # ✅ Catch only SQL-related errors
        print(f"⚠️ Database Error: {e}")
        return DEFAULT_RSS_FEEDS  # ✅ Fallback to default list
    except ValueError as e:  # ✅ Catch missing feeds separately
        print(f"⚠️ Warning: {e}")
        return DEFAULT_RSS_FEEDS  # ✅ Fallback

# ✅ Fallback default list with metadata
DEFAULT_RSS_FEEDS = [
    {
        "name": "BBC World News",
        "url": "http://feeds.bbci.co.uk/news/world/rss.xml",
        "category": "World News",
        "language": "English",
        "region": "Global",
        "source_type": "Mainstream",
        "active": True
    },
    {
        "name": "CNN World",
        "url": "http://rss.cnn.com/rss/edition_world.rss",
        "category": "World News",
        "language": "English",
        "region": "Global",
        "source_type": "Mainstream",
        "active": True
    },
    {
        "name": "El País",
        "url": "http://ep00.epimg.net/rss/elpais/portada.xml",
        "category": "General News",
        "language": "Spanish",
        "region": "Spain",
        "source_type": "Mainstream",
        "active": True
    }
]

# ✅ RSS Feeds List
RSS_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    # ✅ Add additional feed URLs as needed...
]
