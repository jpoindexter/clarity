from typing import List, TYPE_CHECKING
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# ✅ Correct Imports
from backend.src.schemas.news import NewsCreate, NewsUpdate, News as NewsSchema  # ✅ Fixed schema import
from backend.src.database.db_connection import get_db  # ✅ Fixed DB import
from backend.src.models.news import News  # ✅ Corrected model import

if TYPE_CHECKING:
    from backend.src.database.db_connection import SessionLocal  # ✅ Allows future type hints

class NewsCRUD:
    def create(self, db: Session, obj_in: NewsCreate):
        """✅ Create a new news item in the database."""
        new_news = News(**obj_in.model_dump())  # ✅ Fixed for Pydantic V2
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return new_news

    def get(self, db: Session, news_id: int):
        """✅ Retrieve a single news item by ID."""
        news_item = db.query(News).filter(News.id == news_id).first()
        if not news_item:
            raise HTTPException(status_code=404, detail="News item not found")
        return news_item

    def get_all_news(self, db: Session) -> List[NewsSchema]:  # ✅ FIXED MISSING FUNCTION
        """✅ Retrieve all news items in the database."""
        news_list = db.query(News).all()
        return [NewsSchema.model_validate(news) for news in news_list]  # ✅ Replaces from_orm()

    def get_list(self, db: Session, skip=0, limit=100):
        """✅ Retrieve a list of news items with pagination."""
        return db.query(News).offset(skip).limit(limit).all()

    def update(self, db: Session, news_id: int, obj_in: NewsUpdate):
        """✅ Update an existing news item."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            raise HTTPException(status_code=404, detail="News item not found")
        for key, value in obj_in.model_dump(exclude_unset=True).items():
            setattr(db_news, key, value)
        db.commit()
        db.refresh(db_news)
        return db_news

    def remove(self, db: Session, news_id: int):
        """✅ Delete a news item."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            raise HTTPException(status_code=404, detail="News item not found")
        db.delete(db_news)
        db.commit()
        return db_news

# ✅ Instance for proper importing
news_crud = NewsCRUD()
