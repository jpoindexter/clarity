# backend/src/rss/__init__.py

"""
RSS Module Initialization
This module handles RSS feed ingestion, parsing, and AI-powered summarization.
"""

from .feed_manager import fetch_rss_feeds
from .feed_parser import parse_feed
from .summarizer import summarize_article

__all__ = ["fetch_rss_feeds", "parse_feed", "summarize_article"]
