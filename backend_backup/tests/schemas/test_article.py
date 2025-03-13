import pytest
from backend.schemas.article import Article, ArticleCreate  
from pydantic import ValidationError
from datetime import datetime, timezone

def test_article_schema():
    """✅ Ensure Article schema validation works."""

    article = Article(
        id=1,
        title="Test Article",
        summary="This is a test summary.",
        content="Some content",
        source="News",
        url="https://example.com",
        published_at=datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    )

    assert article.title == "Test Article"

    invalid_data = {
        "title": "",  # ❌ Invalid title (empty)
        "summary": "A sample summary.",
        "content": "This is a sample article content.",
        "source": "Author Name",
        "url": "https://example.com",
        "published_at": "2023-01-01T00:00:00+00:00"
    }

    with pytest.raises(ValidationError):
        ArticleCreate(**invalid_data)