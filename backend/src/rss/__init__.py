# backend/src/rss/__init__.py

"""
RSS Module Initialization
This module handles RSS feed ingestion, parsing, and AI-powered summarization.
"""

from .rss_feeds import fetch_rss_feeds
from .feed_parser import fetch_rss_feed as parse_feed
from .summarizer import summarize_text as summarize_article

__all__ = ["fetch_rss_feeds", "parse_feed", "summarize_article"]
