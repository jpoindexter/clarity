from datetime import datetime
from typing import Optional, List

from sqlalchemy.orm import Session

from backend.src.models.news import News
from backend.src.schemas.news import News as NewsSchema  # ✅ Fixed import
from backend.src.schemas.news import NewsCreate, NewsUpdate


class NewsCRUD:
    """✅ CRUD operations for news items."""

    def create(self, db: Session, obj_in: NewsCreate) -> NewsSchema:
        """✅ Create a new news item."""
        new_news = News(
            title=obj_in.title,
            content=obj_in.content,
            source=obj_in.source,
            url=obj_in.url,
            published_at=obj_in.published_at or datetime.utcnow(),  # ✅ Ensure timestamp exists
        )
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return NewsSchema.model_validate(new_news)

    def get(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Retrieve a single news item."""
        news_item = db.query(News).filter(News.id == news_id).first()
        return NewsSchema.model_validate(news_item) if news_item else None

    def get_all_news(self, db: Session) -> List[NewsSchema]:
        """✅ Retrieve all news items."""
        news_list = db.query(News).all()
        return [NewsSchema.model_validate(news) for news in news_list]

    def update(self, db: Session, news_id: int, obj_in: NewsUpdate) -> Optional[NewsSchema]:
        """✅ Update an existing news item."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None

        update_data = obj_in.model_dump(exclude_unset=True)  # ✅ Correct way to update selectively
        for key, value in update_data.items():
            setattr(db_news, key, value)

        db.commit()
        db.refresh(db_news)
        return NewsSchema.model_validate(db_news)

    def remove(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Delete a news item and return it if successful."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None

        db.delete(db_news)
        db.commit()
        return NewsSchema.model_validate(db_news)


# ✅ Singleton instance for usage in API endpoints
news_crud = NewsCRUD()