# backend/src/utils/__init__.py

"""
Utils Module Initialization
This module provides helper functions, logging, and utilities for AI News backend.
"""

from .logger import setup_logger
from .helpers import clean_text, generate_slug
from .timer import Timer

__all__ = ["setup_logger", "clean_text", "generate_slug", "Timer"]
