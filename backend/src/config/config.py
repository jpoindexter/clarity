import os
from dotenv import load_dotenv
from backend.src.rss.rss_feeds import RSS_FEEDS  # Ensure this import is correct

# Load environment variables from .env file (if present)
load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/ai_news_db")

# FastAPI Configuration
API_TITLE = "AI News API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "An AI-powered news aggregation and analysis platform."

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# RSS Feeds Configuration (Now from `rss_feeds.py`, not DB)
try:
    RSS_FEEDS = RSS_FEEDS  # ✅ Pull feeds directly from rss_feeds.py
except Exception as e:
    print(f"⚠️ Warning: Failed to load RSS feeds. Error: {e}")
    RSS_FEEDS = []  # Fallback to an empty list

# AI Processing Configuration
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
ENABLE_SUMMARIZATION = os.getenv("ENABLE_SUMMARIZATION", "true").lower() == "true"

# CORS Configuration
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# Other Global Settings
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", "600"))  # 10 minutes by default

if __name__ == "__main__":
    print(f"🔧 Config Loaded: {API_TITLE} v{API_VERSION}")
    print(f"📡 RSS Feeds Loaded: {len(RSS_FEEDS)} sources")
