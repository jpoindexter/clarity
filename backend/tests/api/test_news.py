
from fastapi.testclient import TestClient
from config.config import settings
from main import app  # ✅ Correct inside pytest

client = TestClient(app)

def test_news_endpoint():
    response = client.get("/news")
    assert response.status_code == 200