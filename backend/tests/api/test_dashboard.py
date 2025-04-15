from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_get_dashboard_summary():
    response = client.get("/api/dashboard/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_articles" in data
    assert "flagged_articles" in data
    assert "last_updated" in data
    assert "top_sources" in data
    assert isinstance(data["top_sources"], list)
