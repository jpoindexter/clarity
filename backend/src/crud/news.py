from typing import List, TYPE_CHECKING
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# ✅ Correct Imports
from src.schemas.news import NewsCreate, NewsUpdate, News as NewsSchema  # ✅ Correct schema import
from src.database.db_connection import get_db  # ✅ Fixed DB import
from src.models.news import News  # ✅ Corrected model import

if TYPE_CHECKING:
    pass  # ✅ Keeps block valid while allowing future type hints

class NewsCRUD:
    def create_news(self, db: Session, news_data: NewsCreate):
        """Create a new news item in the database."""
        new_news = News(**news_data.model_dump())  # ✅ Fixed for Pydantic V2
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return new_news

    def get_news(self, db: Session, news_id: int):
        """Retrieve a single news item by ID."""
        return db.query(News).filter(News.id == news_id).first()

    def get_news_list(self, db: Session, skip=0, limit=100):
        """Retrieve a list of news items with pagination."""
        return db.query(News).offset(skip).limit(limit).all()

    def update_news(self, db: Session, news_id: int, news_data: NewsUpdate):
        """Update an existing news item."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None
        for key, value in news_data.model_dump().items():
            setattr(db_news, key, value)
        db.commit()
        db.refresh(db_news)
        return db_news

    def delete_news(self, db: Session, news_id: int):
        """Delete a news item."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None
        db.delete(db_news)
        db.commit()
        return db_news

# ✅ Define `news` instance for imports
news = NewsCRUD()
