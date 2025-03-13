"""
This module contains a test for the DATABASE_URL configuration.
"""

from backend.src.config.config import DATABASE_URL, BACKEND_HOST, BACKEND_PORT


def test_database_url():
    """
    Test to ensure that the DATABASE_URL setting is not None.

    This test checks that the DATABASE_URL configuration setting is properly set
    and not None. This is important to ensure that the application has the necessary
    database connection information.
    """
    assert settings.DATABASE_URL is not None
