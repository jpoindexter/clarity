from backend.database.db_helper import fetch_articles


def test_fetch_articles(db_session):
    articles = fetch_articles(db_session)
    assert isinstance(articles, list)