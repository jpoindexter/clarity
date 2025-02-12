from typing import List, TYPE_CHECKING
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# ✅ Always import these normally so they work at runtime
from backend.src.schemas.content import ArticleCreate, Article as ArticleSchema  # ✅ Correct import for schemas
from database.db_connection import get_db  # ✅ Fixed import
from models.article import Article  # ✅ Ensure the model is properly imported

if TYPE_CHECKING:
    pass  # ✅ Keeps the block valid while allowing future type hints

class NewsCRUD:
    def create_news(self, db: Session, news_data: ArticleCreate):
        """Create a new news item in the database."""
        new_news = Article(**news_data.model_dump())  # ✅ Fixed for Pydantic V2
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return new_news

    def get_news(self, db: Session, news_id: int):
        """Retrieve a single news item by ID."""
        return db.query(Article).filter(Article.id == news_id).first()

    def get_news_list(self, db: Session, skip=0, limit=100):
        """Retrieve a list of news items with pagination."""
        return db.query(Article).offset(skip).limit(limit).all()

    def update_news(self, db: Session, news_id: int, news_data: ArticleCreate):
        """Update an existing news item."""
        db_news = db.query(Article).filter(Article.id == news_id).first()
        if not db_news:
            return None
        for key, value in news_data.model_dump().items():
            setattr(db_news, key, value)
        db.commit()
        db.refresh(db_news)
        return db_news

    def delete_news(self, db: Session, news_id: int):
        """Delete a news item."""
        db_news = db.query(Article).filter(Article.id == news_id).first()
        if not db_news:
            return None
        db.delete(db_news)
        db.commit()
        return db_news

# ✅ Define `news` instance for imports
news = NewsCRUD()
