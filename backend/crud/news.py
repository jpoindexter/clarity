from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import Session
from backend.models.news import News as NewsModel
from backend.schemas.news import News as NewsSchema
from backend.schemas.news import NewsCreate, NewsUpdate

 
class NewsCRUD:
    """✅ CRUD operations for news items."""

    def create(self, db: Session, obj_in: NewsCreate) -> NewsSchema:
        """✅ Create a new news item."""
        new_news = NewsModel(
            title=obj_in.title,
            content=obj_in.content,
            source=obj_in.source,
            url=obj_in.url,
            published_at=obj_in.published_at or datetime.utcnow(),
        )
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return new_news  # ✅ Return ORM instance for internal use

    def get(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Retrieve a single news item."""
        news_item = db.query(NewsModel).filter(NewsModel.id == news_id).first()
        if news_item:
            return NewsSchema.model_validate(news_item.__dict__)  # ✅ FIXED
        return None

    def get_all(self, db: Session) -> List[NewsSchema]:
        """✅ Retrieve all news items."""
        news_list = db.query(NewsModel).all()
        return [
            NewsSchema.model_validate(news.__dict__)
            for news in news_list
        ]  # ✅ FIXED

    def search(self, db: Session, query: str) -> List[NewsSchema]:
        """✅ Search for news articles by title or content."""
        news_list = db.query(NewsModel).filter(
            (NewsModel.title.ilike(f"%{query}%")) |
            (NewsModel.content.ilike(f"%{query}%"))
        ).all()
        return [
            NewsSchema.model_validate(news.__dict__)
            for news in news_list
        ]  # ✅ FIXED

    def update(
        self, db: Session, db_obj: NewsModel, obj_in: NewsUpdate
    ) -> NewsSchema:
        """✅ Update an existing news item using an existing ORM object."""
        update_data = obj_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)

        db.commit()
        db.refresh(db_obj)
        return NewsSchema.model_validate(db_obj)  # Updated line

    def remove(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Delete a news item and return it if successful."""
        db_news = db.query(NewsModel).filter(NewsModel.id == news_id).first()
        if not db_news: 
            return None

        db.delete(db_news)
        db.commit()
        return NewsSchema.model_validate(db_news.__dict__)  # ✅ FIXED


# ✅ Singleton instance for usage in API endpoints
news_crud = NewsCRUD()

__all__ = ["news_crud", "NewsCRUD"]
