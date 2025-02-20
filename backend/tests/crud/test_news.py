import pytest
from fastapi.testclient import TestClient

from backend.src.api.main import app
from backend.src.database.db_connection import get_db
from backend.src.models.news import News

client = TestClient(app)


@pytest.fixture(scope="function")
def test_db():
    """✅ Clears & resets the test DB before running."""
    db = next(get_db())
    db.query(News).delete()
    db.commit()
    yield db
    db.close()


def test_create_news_missing_fields(test_db):
    """✅ Ensure API returns 422 for missing fields."""
    payload = {"title": "Missing Content"}
    response = client.post("/api/v1/news/", json=payload)
    assert response.status_code == 422


def test_get_news_empty_db(test_db):
    """✅ Ensure API returns an empty list when no news exist."""
    response = client.get("/api/v1/news/")
    assert response.status_code == 200
    assert response.json()["articles"] == []


def test_create_and_get_news(test_db):
    """✅ Ensure created news items can be retrieved correctly."""
    payload = {
        "title": "Breaking News",
        "content": "AI disrupts the world",
        "source": "TechRadar",
        "url": "http://example.com",
    }
    response = client.post("/api/v1/news/", json=payload)
    assert response.status_code == 201
    news_id = response.json()["id"]

    response = client.get(f"/api/v1/news/{news_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Breaking News"


def test_update_nonexistent_news(test_db):
    """✅ Ensure updating a non-existing news entry returns 404."""
    update_payload = {"title": "Updated Title"}
    response = client.put("/api/v1/news/9999", json=update_payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "News item not found"


def test_delete_nonexistent_news(test_db):
    """✅ Ensure deleting a non-existing news entry returns 404."""
    response = client.delete("/api/v1/news/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "News item not found"


def test_delete_existing_news(test_db):
    """✅ Ensure an existing news item is deleted successfully."""
    payload = {
        "title": "News to Delete",
        "content": "This will be removed",
        "source": "News Daily",
        "url": "http://example.com",
    }
    response = client.post("/api/v1/news/", json=payload)
    assert response.status_code == 201
    news_id = response.json()["id"]

    response = client.delete(f"/api/v1/news/{news_id}")
    assert response.status_code == 200

    response = client.get(f"/api/v1/news/{news_id}")
    assert response.status_code == 404


def test_get_news_pagination(test_db):
    """✅ Ensure API returns paginated results correctly."""
    response = client.get("/api/v1/news/?skip=0&limit=1")
    assert response.status_code == 200
    assert isinstance(response.json()["articles"], list)


def test_update_news_invalid_data(test_db):
    """✅ Ensure updating a news item with invalid data fails."""
    news_item = News(
        title="Update Test",
        content="Before update",
        source="Test Source",
        url="https://test.com/update",
    )
    test_db.add(news_item)
    test_db.commit()
    test_db.refresh(news_item)

    update_payload = {}
    response = client.put(f"/api/v1/news/{news_item.id}", json=update_payload)
    assert response.status_code == 422


def test_delete_already_deleted_news(test_db):
    """✅ Ensure deleting already deleted news does not crash."""
    news_item = News(
        title="Delete Test",
        content="Will be deleted",
        source="Test Source",
        url="https://test.com/delete",
    )
    test_db.add(news_item)
    test_db.commit()
    test_db.refresh(news_item)

    client.delete(f"/api/v1/news/{news_item.id}")

    response = client.delete(f"/api/v1/news/{news_item.id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "News item not found"
