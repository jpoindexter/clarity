# backend/tests/api/test_fetch.py
from fastapi.testclient import TestClient
from backend.src.main import app

client = TestClient(app)

def test_fetch_endpoint():
    response = client.get("/fetch")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
