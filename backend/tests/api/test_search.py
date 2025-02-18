import pytest
from fastapi.testclient import TestClient
from backend.src.api.main import app

client = TestClient(app)

def test_search_articles():
    """Test the search API endpoint."""
    response = client.get("/api/v1/search", params={"q": "Tech"})
    assert response.status_code == 200, "❌ API failed"
    assert "results" in response.json(), "❌ No results in response"