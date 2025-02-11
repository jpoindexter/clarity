from src.utils.db_helper import fetch_articles

def test_fetch_articles():
    articles = fetch_articles()
    assert isinstance(articles, list)