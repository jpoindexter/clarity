from fastapi.testclient import TestClient
from backend.main import app  # ✅ Corrected import (removed backend.src)
from backend.database.db_connection import get_db  # ✅ Corrected import  # ✅ Correct import
import pytest

client = TestClient(app)  # ✅ Uses FastAPI TestClient

@pytest.mark.usefixtures("test_db")  # ✅ Ensure we use the test database
def test_news_endpoint():
    response = client.get("/api/news/")  # ✅ Ensure correct URL
    assert response.status_code == 200  # ✅ Should now work
