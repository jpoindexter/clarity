import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_fetch_endpoint():
    response = client.get("/fetch")
    assert response.status_code == 200