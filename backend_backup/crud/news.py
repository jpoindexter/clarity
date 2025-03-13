from typing import List, Optional
from sqlalchemy.orm import Session

from backend.models.news import News as NewsModel
from backend.schemas.news import NewsCreate, NewsUpdate, NewsSchema


class NewsCRUD:
    """CRUD operations for News."""

    @staticmethod
    def get_news(db: Session, news_id: int) -> Optional[NewsSchema]:
        """Retrieve a specific news article by ID."""
        return db.query(NewsModel).filter(NewsModel.id == news_id).first()

    @staticmethod
    def get_all_news(db: Session) -> List[NewsSchema]:
        """Retrieve all news articles."""
        return db.query(NewsModel).all()

    @staticmethod
    def create_news(db: Session, news: NewsCreate) -> NewsSchema:
        """Create a new news entry."""
        db_news = NewsModel(**news.dict())
        db.add(db_news)
        db.commit()
        db.refresh(db_news)
        return db_news

    @staticmethod
    def update_news(
        db: Session, news_id: int, news: NewsUpdate
    ) -> Optional[NewsSchema]:
        """Update an existing news entry."""
        db_news = db.query(NewsModel).filter(NewsModel.id == news_id).first()
        if not db_news:
            return None
        for key, value in news.dict(exclude_unset=True).items():
            setattr(db_news, key, value)
        db.commit()
        db.refresh(db_news)
        return db_news

    @staticmethod
    def delete_news(db: Session, news_id: int) -> bool:
        """Delete a news entry."""
        db_news = db.query(NewsModel).filter(NewsModel.id == news_id).first()
        if not db_news:
            return False
        db.delete(db_news)
        db.commit()
        return True


# ✅ Define news_crud object for importing
news_crud = NewsCRUD()

__all__ = ["news_crud", "NewsCRUD"]
