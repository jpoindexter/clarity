"""
This module contains a test for the DATABASE_URL configuration.
"""

from backend.config.config import settings


def test_database_url():
    """
    Test to ensure that the DATABASE_URL setting is properly configured.

    This test checks that the DATABASE_URL configuration setting is:
    1. Not None
    2. A valid non-empty string
    3. A properly formatted database URL
    """
    assert settings.DATABASE_URL is not None, "DATABASE_URL should not be None"
    assert isinstance(settings.DATABASE_URL, str) and settings.DATABASE_URL.strip(), (
        "DATABASE_URL should be a non-empty string"
    )
    assert (settings.DATABASE_URL.startswith("postgresql") or
            settings.DATABASE_URL.startswith("sqlite")), (
        "DATABASE_URL should start with a valid database scheme"
    )
