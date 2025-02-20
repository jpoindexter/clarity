from backend.src.models.article import Article

def test_articles(test_db):
    """✅ Ensure Article model works correctly"""
    article = Article(title="Test Title", content="Test Content")
    test_db.add(article)
    test_db.commit()
    test_db.refresh(article)
    
    assert article.title == "Test Title"
    assert article.content == "Test Content"
    assert article.id is not None

    fetched_article = test_db.query(Article).get(article.id)
    assert fetched_article.title == "Test Title"
    assert fetched_article.content == "Test Content"

    test_db.delete(article)
    test_db.commit()
    assert test_db.query(Article).get(article.id) is None