"""
This module contains a test for the DATABASE_URL configuration.
"""

from config.config import DATABASE_URL

def test_database_url():
    assert DATABASE_URL is not None