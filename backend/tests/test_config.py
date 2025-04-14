"""This module contains a test for the DATABASE_URL configuration.
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
    assert settings.database_url is not None, "database_url should not be None"
    assert isinstance(settings.database_url, str) and settings.database_url.strip(), (
        "database_url should be a non-empty string"
    )
    assert (settings.database_url.startswith("postgresql://") or
            settings.database_url.startswith("sqlite://")), (
        "database_url should start with a valid database scheme"
    )