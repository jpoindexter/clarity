"""
Test cases for the /news API endpoint.

This module tests whether the /news endpoint in the FastAPI application 
returns the expected responses.
"""

from fastapi.testclient import TestClient
from main import app  # ✅ Still needed

client = TestClient(app)

def test_news_endpoint():
    """Test that the /news endpoint returns a 200 status code."""
    response = client.get("/news")
    assert response.status_code == 200
