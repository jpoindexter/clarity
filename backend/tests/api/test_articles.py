import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime

from backend.src.main import app
from backend.src.database.db_connection import get_db
from backend.src.crud.news import news_crud
from backend.src.utils.detect_misinfiromation import detect_misinformation  # ✅ Fixed import
from backend.src.utils.summarizer import summarize  # ✅ Updated import
from backend.src.schemas.news import NewsCreate

# ✅ Create a test client for API testing
client = TestClient(app)

# ✅ Setup a test database session
@pytest.fixture(scope="module")
def db():
    """Provide a test database session."""
    test_db = next(get_db())  # ✅ Get a fresh test DB session
    yield test_db
    test_db.close()  # ✅ Ensure session closes properly

# ✅ Test misinformation detection function
def test_detect_misinformation():
    """✅ Test AI-powered misinformation detection."""
    result = detect_misinformation("This is fake news.")
    assert isinstance(result, dict), "Result should be a dictionary."
    assert "misinformation_score" in result, "Missing 'misinformation_score' key in response."

# ✅ Test the analyze_news endpoint
def test_analyze_news(db: Session):
    """✅ Ensure AI analysis works on news articles."""
    news_data = {
        "title": "Test News Article",
        "content": "This is a test article.",
        "source": "Test Source",
        "url": "https://example.com/test-news",
        "published_at": datetime.utcnow(),  # ✅ Ensure valid timestamp
    }
    created_news = news_crud.create(db, obj_in=NewsCreate(**news_data))

    response = client.get(f"/news/analyze/{created_news.id}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    assert "misinformation_analysis" in data, "Missing 'misinformation_analysis' in response."

# ✅ Test summarization function
def test_summarization():
    """✅ Ensure text summarization works correctly."""
    text = "This is a long article that needs summarization."
    summary = summarize(text)
    
    assert isinstance(summary, str), "Summary should be a string."
    assert len(summary) > 0, "Summary should not be empty."
