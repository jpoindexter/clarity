import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

# ✅ Import API & DB components
from backend.src.api.main import app
from backend.src.database.db_connection import get_db
from backend.src.models.news import News
from backend.src.schemas.news import NewsCreate, NewsUpdate
from backend.src.crud.news import news_crud  # ✅ Import CRUD instance for direct DB interaction

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

def test_get_news_empty_db(test_db):
    """✅ Ensure API returns an empty list when no news exist"""
    response = client.get("/api/v1/news/")
    assert response.status_code == 200
    assert response.json()["articles"] == []  # ✅ Adjust assertion to match API response

# ✅ Test Creating & Retrieving News
def test_create_and_get_news(test_db):
    """✅ Ensure created news items can be retrieved correctly"""
    payload = {"title": "Breaking News", "content": "AI disrupts the world", "source": "TechRadar", "url": "http://example.com"}
    response = client.post("/api/v1/news/", json=payload)
    assert response.status_code == 201
    news_id = response.json()["id"]

    # ✅ Retrieve newly created news
    response = client.get(f"/api/v1/news/{news_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Breaking News"

# ✅ Test Updating Nonexistent News
def test_update_nonexistent_news(test_db):
    """✅ Ensure updating a non-existing news entry returns 404"""
    update_payload = {"title": "Updated Title"}
    response = client.put("/api/v1/news/9999", json=update_payload)
    assert response.status_code == 404

# ✅ Test Deleting Nonexistent News
def test_delete_nonexistent_news(test_db):
    """✅ Ensure deleting a non-existing news entry returns 404"""
    response = client.delete("/api/v1/news/9999")
    assert response.status_code == 404

# ✅ Test Deleting Existing News
def test_delete_existing_news(test_db):
    """✅ Ensure an existing news item is deleted successfully"""
    payload = {"title": "News to Delete", "content": "This will be removed", "source": "News Daily", "url": "http://example.com"}
    response = client.post("/api/v1/news/", json=payload)
    assert response.status_code == 201
    news_id = response.json()["id"]

    # ✅ Delete the news
    response = client.delete(f"/api/v1/news/{news_id}")
    assert response.status_code == 200

    # ✅ Confirm it's gone
    response = client.get(f"/api/v1/news/{news_id}")
    assert response.status_code == 404
