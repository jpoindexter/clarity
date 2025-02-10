"""
Tests for the `/fetch` API endpoint.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_fetch_endpoint():
    """Tests that the `/fetch` endpoint returns a successful response (200 OK)."""
    response = client.get("/fetch")
    assert response.status_code == 200
