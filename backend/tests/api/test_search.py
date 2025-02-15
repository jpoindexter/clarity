"""
Tests for the `/api/v1/articles/` endpoint.
"""

import pytest
from fastapi.testclient import TestClient
from backend.src.api.main import app  # ✅ Ensure correct import
from backend.src.database.db_connection import get_test_db  # ✅ Use test DB

client = TestClient(app)


@pytest.fixture
def test_db():
    """Provides a test database session."""
    db = next(get_test_db())  # ✅ Use the test DB function
    yield db
    db.close()


@pytest.mark.usefixtures("test_db")  # ✅ Ensure tests use the test database
def test_articles_endpoint():
    """Tests that the `/api/v1/articles/` endpoint returns a successful response (200 OK)."""
    response = client.get("/api/v1/articles/")  # ✅ Updated to match new route
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Response should return a list of articles"
    if response.json():  # ✅ If there are articles, validate structure
        assert "id" in response.json()[0], "Missing 'id' field in article"
        assert "title" in response.json()[0], "Missing 'title' field in article"
        assert "content" in response.json()[0], "Missing 'content' field in article"