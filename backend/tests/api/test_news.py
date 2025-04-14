import pytest
from fastapi.testclient import TestClient
from backend.api.main import app
from backend.database.db_connection import get_db
from backend.models.news import News

# Create a test client for the FastAPI application
client = TestClient(app)


@pytest.fixture(scope="function")
def test_db():
    """✅ Clears & resets the test DB before running"""
    db = next(get_db())
    db.query(News).delete()  # Clear existing data in the database
    db.commit()
    yield db  # Provide the database session to the tests
    db.close()  # Close the session after testing is complete


# Test data with all required fields 
news_data = {
    "title": "Test News Article",
    "content": "This is a test article.",
    "source": "Test Source",
    "url": "https://example.com/test-news-article",  # Added missing field
    "created_at": "2025-02-22T00:00:00Z"  # Ensure timestamp is present
}

# Test creating news without required fields


def test_create_news_missing_fields(test_db):
    payload = {"title": "Missing Content"}
    response = client.post("/api/news/", json=payload)
    assert response.status_code == 422  # Expect validation error

# Test retrieving an empty news list when the database is empty


def test_get_empty_news_list(test_db):
    response = client.get("/api/news/")
    assert response.status_code == 200
    assert len(response.json()["articles"]) == 0

# Test creating news successfully with all required fields


def test_create_news_success(test_db):
    response = client.post("/api/news/", json=news_data)
    assert response.status_code == 201
    assert response.json()["title"] == news_data["title"]
    assert response.json()["content"] == news_data["content"]

# Test retrieving a list of news when there is data in the database


def test_get_news_list(test_db):
    # Add test data to the database
    new_news = News(**news_data)
    test_db.add(new_news)
    test_db.commit()

    response = client.get("/api/news/")
    assert response.status_code == 200
    assert len(response.json()["articles"]) == 1
    assert response.json()["articles"][0]["title"] == news_data["title"]

# Test updating existing news with valid data


def test_update_existing_news(test_db):
    # Add test data to the database
    new_news = News(**news_data)
    test_db.add(new_news)
    test_db.commit()

    updated_data = {"title": "Updated Title", "content": "Updated content."}
    response = client.put(f"/api/news/{new_news.id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == updated_data["title"]
    assert response.json()["content"] == updated_data["content"]

# Test deleting existing news with a valid ID


def test_delete_existing_news(test_db):
    # Add test data to the database
    new_news = News(**news_data)
    test_db.add(new_news)
    test_db.commit()

    response = client.delete(f"/api/news/{new_news.id}")
    assert response.status_code == 204

    # Verify the news item is deleted by trying to retrieve it again
    response = client.get(f"/api/news/{new_news.id}")
    assert response.status_code == 404
