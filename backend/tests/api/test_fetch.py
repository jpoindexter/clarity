"""
Tests for the `/api/articles/` endpoint.
"""

from fastapi.testclient import TestClient
from backend.main import app  # ✅ Ensure correct import

client = TestClient(app)

def test_articles_endpoint():
    """Tests that the `/api/articles/` endpoint returns a successful response (200 OK)."""
    response = client.get("/api/articles/")  # ✅ Updated to match new route
    assert response.status_code == 200
