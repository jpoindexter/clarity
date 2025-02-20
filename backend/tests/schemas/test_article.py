import pytest
from pydantic import ValidationError
from backend.src.schemas.article import Article as ArticleSchema


def test_article_schema():
    """✅ Ensure Article schema validation works."""
    from backend.src.schemas.article import Article  # ✅ Fix import

    article = Article(title="Test Article", content="Some content", source="News", url="https://example.com")
    assert article.title == "Test Article"

    valid_data = {
        "title": "Sample Article",
        "content": "This is a sample article content.",
        "author": "Author Name",
        "published_date": "2023-01-01"
    }

    schema = ArticleSchema(**valid_data)
    assert schema.title == valid_data["title"]
    assert schema.content == valid_data["content"]
    assert schema.author == valid_data["author"]
    assert schema.published_date == valid_data["published_date"]

    invalid_data = {
        "title": "",
        "content": "This is a sample article content.",
        "author": "Author Name",
        "published_date": "2023-01-01"
    }

    with pytest.raises(ValidationError):
        ArticleSchema(**invalid_data)