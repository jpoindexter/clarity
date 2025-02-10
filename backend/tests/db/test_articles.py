# backend/tests/db/test_articles.py
from backend.src.database.db_helper import fetch_articles

def test_fetch_articles():
    articles = fetch_articles()
    assert isinstance(articles, list)
    assert len(articles) > 0
