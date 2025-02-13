"""
Test cases for the /api/news API endpoint.

This module tests whether the /api/news endpoint in the FastAPI application 
returns the expected responses.
"""

from fastapi.testclient import TestClient
from api.main import app  # ✅ Remove `src.` to match actual path

client = TestClient(app)

def test_news_endpoint():
    """Test that the /api/news endpoint returns a 200 status code."""
    response = client.get("/api/news")  # ✅ Matches /api prefix in main.py
    assert response.status_code == 200
