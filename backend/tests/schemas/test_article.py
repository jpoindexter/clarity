def test_article_schema():
    from backend.src.schemas.article import ArticleSchema

    valid_data = {
        "title": "Sample Article",
        "content": "This is a sample article content.",
        "author": "Author Name",
        "published_date": "2023-01-01"
    }

    schema = ArticleSchema()
    result = schema.load(valid_data)
    assert result == valid_data

    invalid_data = {
        "title": "",
        "content": "This is a sample article content.",
        "author": "Author Name",
        "published_date": "2023-01-01"
    }

    try:
        schema.load(invalid_data)
    except Exception as e:
        assert isinstance(e, ValueError)