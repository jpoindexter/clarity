from fastapi.testclient import TestClient

from backend.api.main import app

client = TestClient(app)


def test_search_articles():
    """Test the search API endpoint."""
    response = client.get("/api/search/query", params={"q": "Tech"})
    assert response.status_code == 200, "❌ API failed"
    assert "results" in response.json(), "❌ No results in response"