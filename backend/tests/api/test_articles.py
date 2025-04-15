import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from backend.api.main import app  # ✅ Corrected import path
from backend.database.db_connection import get_db
from backend.crud.news import news_crud
from backend.utils.detect_misinformation import detect_misinformation  # ✅ Fixed import
from backend.utils.summarizer import summarize_text  # ✅ Updated import
from backend.schemas.news import NewsCreate
from backend.models.news import News  # Add this import at the top if not already present

# ✅ Create a test client for API testing
client = TestClient(app)


# ✅ Setup a test database session 
@pytest.fixture(scope="module")
def db():
    """Provide a test database session."""
    test_db = next(get_db())  # ✅ Fetch a fresh session
    try:
        yield test_db
    finally:
        test_db.close()  # ✅ Ensure session is properly closed


# ✅ Test misinformation detection function
def test_detect_misinformation():
    """✅ Test AI-powered misinformation detection."""
    result = detect_misinformation("This is fake news.")
    assert isinstance(result, dict), "Result should be a dictionary."
    assert "misinformation_score" in result.keys(
    ), "Missing 'misinformation_score' key in response."


# ✅ Test the analyze_news endpoint 
def test_analyze_news(db: Session):
    """✅ Ensure AI analysis works on news articles."""
    news_data = {
        "title": "Test News Article",
        "content": "This is a test article.",
        "source": "Test Source",
        "url": "https://example.com/test-news",
        "published_at": datetime.utcnow(),
    }
    # Use raw SQLAlchemy model and skip .refresh()
    new_article = News(**news_data)
    db.add(new_article)
    db.commit() 

    response = client.get(f"/news/analyze/{new_article.id}")
    assert response.status_code == 200, (
        f"Unexpected status code: {response.status_code}"
    )
    data = response.json()
    assert "misinformation_analysis" in data, "Missing 'misinformation_analysis' in response."


# ✅ Test summarization function
def test_summarization():
    """✅ Ensure text summarization works correctly."""
    text = "This is a long article that needs summarization."
    summary = summarize_text(text)

    assert isinstance(summary, str), "Summary should be a string."
    assert len(summary) > 0, "Summary should not be empty."

def test_ingest_article_url():
    """✅ Test article ingestion via URL and summarization."""
    response = client.post("/api/articles/ingest", json={
        "source": "url",
        "input": "https://example.com"
    })
    assert response.status_code == 200, f"Unexpected status: {response.status_code}"
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "No article summaries returned"
    assert "summary" in data[0], "Missing 'summary' in response"
    assert "url" in data[0], "Missing 'url' in response"
