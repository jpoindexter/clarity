# backend/tests/test_config.py
import os
from backend.src.config.config import DATABASE_URL

def test_database_url():
    assert isinstance(DATABASE_URL, str)
    assert "postgresql" in DATABASE_URL.lower()

# Run with `pytest backend/tests/test_config.py`
