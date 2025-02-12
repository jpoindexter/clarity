"""
Configuration settings for the FastAPI project.

This module loads environment variables and defines application-wide settings.
"""

import os
from src.dotenv import load_dotenv
from src.rss.rss_feeds import RSS_FEEDS  # ✅ Ensure correct path

# ✅ Load environment variables from .env file (if present)
load_dotenv()


class Config:
    """Global Configuration Settings"""

    # ✅ Database Configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://jpoindexter:dontforgetme@localhost:5432/ai_news_db"
    )

    # ✅ FastAPI Configuration
    API_TITLE: str = "AI News API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "An AI-powered news aggregation and analysis platform."

    # ✅ Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # ✅ RSS Feeds Configuration (Safe Fallback)
    try:
        RSS_FEEDS = RSS_FEEDS  # ✅ Load from `rss_feeds.py`
    except (ImportError, ValueError) as e:  # ✅ More specific
        print(f"⚠️ Warning: Failed to load RSS feeds. Error: {e}")
        RSS_FEEDS = []  # Fallback to empty list

    # ✅ AI Processing Configuration
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral")
    ENABLE_SUMMARIZATION: bool = os.getenv("ENABLE_SUMMARIZATION", "true").lower() == "true"

    # ✅ CORS Configuration (Parses Allowed Origins Safely)
    ALLOWED_ORIGINS: list[str] = os.getenv("ALLOWED_ORIGINS", "*").split(",")

    # ✅ Other Global Settings
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"
    FETCH_INTERVAL: int = int(os.getenv("FETCH_INTERVAL", "600"))  # 10 minutes default


# ✅ Create a global settings instance
settings = Config()

# ✅ Debug Output
if __name__ == "__main__":
    print(f"🔧 Config Loaded: {settings.API_TITLE} v{settings.API_VERSION}")
    print(f"📡 RSS Feeds Loaded: {len(settings.RSS_FEEDS)} sources")
    print(f"🌍 Allowed Origins: {settings.ALLOWED_ORIGINS}")
    print(f"⚡ Debug Mode: {'ON' if settings.DEBUG_MODE else 'OFF'}")
