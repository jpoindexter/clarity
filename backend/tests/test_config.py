import os
from src.config.config import DATABASE_URL

def test_database_url():
    assert DATABASE_URL is not None