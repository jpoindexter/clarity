import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

# ✅ Correct absolute imports
from backend.src.api.main import app
from backend.src.config import settings
from backend.src.crud.news import news_crud
from backend.src.database.db_connection import get_db

client = TestClient(app)

@pytest.fixture
def test_db():
    """Provides a test database session."""
    db = next(get_db())  # ✅ Corrected how the DB session is retrieved
    yield db
    db.close()