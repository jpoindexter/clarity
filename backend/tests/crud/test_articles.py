from datetime import datetime, timezone
from backend.src.models.article import Article

def test_articles(test_db):
    """✅ Ensure Article model works correctly"""

    # ✅ Include all required fields with timezone-aware datetime
    article = Article(
        title="Test Title",
        summary="Test Summary",
        content="Test Content",
        source="Test Source",
        url="https://example.com/test-article",
        published_at=datetime.now(timezone.utc),  # 🔹 FIXED: Use timezone-aware datetime
    )

    test_db.add(article)
    test_db.commit()
    test_db.refresh(article)

    # ✅ Ensure data is correctly stored
    assert article.title == "Test Title"
    assert article.summary == "Test Summary"
    assert article.content == "Test Content"
    assert article.source == "Test Source"
    assert article.url == "https://example.com/test-article"
    assert article.published_at is not None
    assert article.id is not None

    # ✅ Fetch and verify stored article
    fetched_article = test_db.query(Article).filter_by(id=article.id).first()
    assert fetched_article is not None
    assert fetched_article.title == "Test Title"
    assert fetched_article.summary == "Test Summary"
    assert fetched_article.content == "Test Content"
    assert fetched_article.source == "Test Source"
    assert fetched_article.url == "https://example.com/test-article"

    # ✅ Cleanup: Delete article and confirm deletion
    test_db.delete(article)
    test_db.commit()
    assert test_db.query(Article).filter_by(id=article.id).first() is None
