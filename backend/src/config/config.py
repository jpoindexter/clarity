"""
Configuration settings for the FastAPI project.

This module loads environment variables and defines application-wide settings.
"""

import os
from typing import ClassVar, List
from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict

load_dotenv()

try:
    from backend.src.rss.rss_feeds import RSS_FEEDS
except ImportError as e:
    print(f"⚠️ Warning: Failed to import RSS feeds. Error: {e}")
    RSS_FEEDS = []


class Config(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    RSS_FEEDS: ClassVar[List[str]] = []
    ALLOWED_ORIGINS_RAW: ClassVar[str] = "http://127.0.0.1:3000,http://localhost:3000"

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://jpoindexter:dontforgetme@localhost:5432/ai_news_db",
    )

    API_TITLE: str = "AI News API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "An AI-powered news aggregation and analysis platform."

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    RSS_FEEDS = RSS_FEEDS

    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral")
    ENABLE_SUMMARIZATION: bool = (
        os.getenv("ENABLE_SUMMARIZATION", "true").lower() == "true"
    )

    ALLOWED_ORIGINS_RAW = os.getenv("ALLOWED_ORIGINS", "*")
    ALLOWED_ORIGINS: list[str] = (
        ALLOWED_ORIGINS_RAW.split(",") if ALLOWED_ORIGINS_RAW else ["*"]
    )

    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"
    FETCH_INTERVAL: int = int(os.getenv("FETCH_INTERVAL", "600"))

    @classmethod
    def debug(cls):
        print(f"🔧 Config Loaded: {cls.API_TITLE} v{cls.API_VERSION}")
        print(f"📡 RSS Feeds Loaded: {len(cls.RSS_FEEDS)} sources")
        print(f"🌍 Allowed Origins: {cls.ALLOWED_ORIGINS}")
        print(f"⚡ Debug Mode: {'ON' if cls.DEBUG_MODE else 'OFF'}")


settings = Config()

if __name__ == "__main__":
    settings.debug()
