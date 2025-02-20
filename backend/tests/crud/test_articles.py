def test_articles():
    from backend.src.crud.articles import Article

    article = Article(title="Test Title", content="Test Content")
    assert article.title == "Test Title"
    assert article.content == "Test Content"

    article.save()
    assert article.id is not None

    fetched_article = Article.get(article.id)
    assert fetched_article.title == "Test Title"
    assert fetched_article.content == "Test Content"

    article.delete()
    assert Article.get(article.id) is None