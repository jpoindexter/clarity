"""
Test database connection and queries.
"""

import pytest
from backend.src.database.db_connection import get_db
from backend.src.crud.articles import fetch_articles  # ✅ Correct import

@pytest.fixture(scope="module")
def test_db():
    """Provides a test database session."""
    db = next(get_db())  # ✅ Correctly fetch a session
    yield db
    db.close()

def test_db_connection(test_db):
    """Ensure that the database connection is established properly."""
    assert test_db is not None, "Database connection failed"

def test_fetch_articles(test_db):
    """Test if querying articles returns a list."""
    articles = fetch_articles(test_db)  # ✅ Pass `test_db` session
    assert isinstance(articles, list), "fetch_articles() did not return a list"