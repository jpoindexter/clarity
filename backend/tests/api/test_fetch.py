"""
Tests for the `/api/articles/` endpoint.
"""

from fastapi.testclient import TestClient

from backend.src.api.main import app  # ✅ Fix path to match structure

client = TestClient(app)


def test_articles_endpoint():
    """
    ✅ Tests that the `/api/articles/` endpoint returns
    a successful response (200 OK).
    """
    response = client.get("/api/v1/articles/")  # ✅ Correct route
    assert response.status_code == 200
