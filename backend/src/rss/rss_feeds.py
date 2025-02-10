from backend.src.database.db_helper import get_rss_feeds

def fetch_rss_feeds():
    """Fetch the latest RSS feeds from the database"""
    try:
        feeds = get_rss_feeds()  # Fetch from database
        if not feeds:
            raise ValueError("No feeds found in DB. Falling back to default list.")
        return feeds
    except Exception as e:
        print(f"⚠️ Warning: {e}")
        return DEFAULT_RSS_FEEDS  # Fallback to hardcoded list

# Fallback default list with metadata (for emergency use)
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

# Load RSS feeds (use DB if available, otherwise fallback)
RSS_FEEDS = fetch_rss_feeds()
