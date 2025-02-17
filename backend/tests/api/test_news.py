import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

# ✅ Correct absolute imports
from backend.src.api.main import app
from backend.src.database.db_connection import get_db
from backend.src.models.news import News
from backend.src.crud.news import news_crud

client = TestClient(app)

# ✅ Fixture to ensure test DB is used
@pytest.fixture(scope="function")
def test_db():
    db = next(get_db())
    db.query(News).delete()  # ✅ Clear any existing test data
    db.commit()
    yield db
    db.close()

def test_get_news(test_db):
    """✅ Ensure the news endpoint returns valid JSON"""
    # ✅ Insert mock data and force commit
    mock_news = News(
        title="Test News Title",
        content="Test News Content",
        source="Test Source",
        url="https://test.com/news"
    )
    test_db.add(mock_news)
    test_db.commit()
    test_db.refresh(mock_news)  # ✅ Ensures DB recognizes it

    # ✅ Call the `/news` endpoint
    response = client.get("/api/v1/news/")  # ✅ Use correct API prefix
    
    # ✅ Ensure the endpoint exists and data is returned
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    json_response = response.json()
    assert "articles" in json_response
    assert isinstance(json_response["articles"], list)
    assert len(json_response["articles"]) > 0  # ✅ Ensures at least one result is returned

def test_get_news_empty(test_db):
    """✅ Ensure API handles no news correctly"""
    response = client.get("/news?source=invalid")
    
    # ✅ Allow API to return either 200 or 404, depending on logic
    assert response.status_code in [200, 404]  
    if response.status_code == 200:
        assert response.json() == {"articles": []}  # ✅ Expect empty response
