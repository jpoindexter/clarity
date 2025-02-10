import pytest
from fastapi.testclient import TestClient
from src.config.config import settings
from src.main import app

client = TestClient(app)

def test_news_endpoint():
    response = client.get("/news")
    assert response.status_code == 200