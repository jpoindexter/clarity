"""
Configuration settings for the FastAPI project.

This module loads environment variables and defines application-wide settings.
"""

import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env file (if present)
load_dotenv()

# ✅ Ensure absolute import to avoid circular imports
try:
    from backend.src.rss.rss_feeds import RSS_FEEDS
except ImportError as e:
    print(f"⚠️ Warning: Failed to import RSS feeds. Error: {e}")
    RSS_FEEDS = []  # ✅ Fallback to empty list


class Config:
    """Global Configuration Settings."""

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
    RSS_FEEDS = RSS_FEEDS  # ✅ Ensure RSS Feeds are loaded correctly

    # ✅ AI Processing Configuration
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral")
    ENABLE_SUMMARIZATION: bool = os.getenv("ENABLE_SUMMARIZATION", "true").lower() == "true"

    # ✅ CORS Configuration (Parses Allowed Origins Safely)
    ALLOWED_ORIGINS_RAW = os.getenv("ALLOWED_ORIGINS", "*")
    ALLOWED_ORIGINS: list[str] = ALLOWED_ORIGINS_RAW.split(",") if ALLOWED_ORIGINS_RAW else ["*"]

    # ✅ Other Global Settings
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"
    FETCH_INTERVAL: int = int(os.getenv("FETCH_INTERVAL", "600"))  # Default: 10 minutes

    # ✅ Method to display loaded settings for debugging
    @classmethod
    def debug(cls):
        print(f"🔧 Config Loaded: {cls.API_TITLE} v{cls.API_VERSION}")
        print(f"📡 RSS Feeds Loaded: {len(cls.RSS_FEEDS)} sources")
        print(f"🌍 Allowed Origins: {cls.ALLOWED_ORIGINS}")
        print(f"⚡ Debug Mode: {'ON' if cls.DEBUG_MODE else 'OFF'}")


# ✅ Create a global settings instance
settings = Config()

# ✅ Debug Output (Only runs if script is executed directly)
if __name__ == "__main__":
    settings.debug()