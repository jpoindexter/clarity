import pytest
from backend.crud.news import news_crud
from backend.models.news import News
from backend.schemas.news import NewsCreate, NewsUpdate


def test_create_news(test_db):
    """✅ Ensure news creation works without violating unique constraints"""
    test_db.query(News).delete()  # ✅ Clear existing entries before running test
    test_db.commit()

    news_data = NewsCreate(
        title="Test News",
        content="This is a test news article.",
        source="Test Source",
        url="https://test.com/news"
    )
    news_item = news_crud.create(test_db, obj_in=news_data)
    assert news_item.id is not None


def test_update_news(test_db):
    """✅ Ensure news updates properly"""
    news_item = news_crud.create(
        test_db,
        obj_in=NewsCreate(
            title="Old Title",
            content="Old Content",
            source="Test Source",
            url="https://test.com/news-old"
        ),
    )

    update_data = NewsUpdate(title="New Title")
    updated_news = news_crud.update(test_db, db_obj=news_item, obj_in=update_data)

    assert updated_news.title == "New Title"


def test_delete_news(test_db):
    """✅ Ensure deleting news works"""
    news_item = news_crud.create(
        test_db,
        obj_in=NewsCreate(
            title="Delete Me",
            content="Will be deleted",
            source="Test Source",
            url="https://test.com/delete"
        ),
    )

    deleted_news = news_crud.remove(test_db, news_item.id)
    assert deleted_news is not None
    assert news_crud.get(test_db, news_item.id) is None