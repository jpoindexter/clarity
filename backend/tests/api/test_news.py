import pytest
from fastapi.testclient import TestClient

from backend.src.api.main import app
from backend.src.database.db_connection import get_db
from backend.src.models.news import News

client = TestClient(app)


@pytest.fixture(scope="function")
def test_db():
    """✅ Clears & resets the test DB before running"""
    db = next(get_db())
    db.query(News).delete()
    db.commit()
    yield db
    db.close()


# ✅ Test Creating News Without Required Fields
def test_create_news_missing_fields(test_db):
    """✅ Ensure API returns 422 for missing fields"""
    payload = {"title": "Missing Content"}
    response = client.post("/api/v1/news/", json=payload)
    assert response.status_code == 422  # ✅ Expect validation error


# ✅ Test Retrieving Empty News List
def test_get_news_empty_db(test_db):
    """✅ Ensure API returns an empty list when no news exists"""
    response = client.get("/api/v1/news/")
    assert response.status_code == 200
    assert response.json()["articles"] == []  # ✅ Match actual API response


# ✅ Test Updating Nonexistent News
def test_update_nonexistent_news(test_db):
    """✅ Ensure updating a non-existing news entry returns 404"""
    update_payload = {"title": "Updated Title"}
    response = client.put("/api/v1/news/9999", json=update_payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "News item not found"


# ✅ Test Deleting Nonexistent News
def test_delete_nonexistent_news(test_db):
    """✅ Ensure deleting a non-existing news entry returns 404"""
    response = client.delete("/api/v1/news/9999")
    assert response.status_code == 404


# ✅ Test Retrieving Nonexistent News
def test_get_nonexistent_news(test_db):
    """✅ Ensure API returns 404 for non-existing news item"""
    response = client.get("/api/v1/news/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "News item not found"
