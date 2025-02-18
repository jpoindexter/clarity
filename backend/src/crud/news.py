from typing import List, TYPE_CHECKING, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session

# ✅ Correct Imports
from backend.src.schemas.news import NewsCreate, NewsUpdate, News as NewsSchema  
from models.news import News  

if TYPE_CHECKING:
    from backend.src.database.db_connection import SessionLocal  

class NewsCRUD:
    def create(self, db: Session, obj_in: NewsCreate) -> NewsSchema:
        """✅ Create a new news item in the database."""
        new_news = News(**obj_in.model_dump())
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return NewsSchema.model_validate(new_news)  

    def get(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Retrieve a single news item by ID."""
        news_item = db.query(News).filter(News.id == news_id).first()
        if not news_item:
            return None  
        return NewsSchema.model_validate(news_item)  

    def get_all_news(self, db: Session) -> List[NewsSchema]:  
        """✅ Retrieve all news items in the database."""
        news_list = db.query(News).all()
        return [NewsSchema.model_validate(news) for news in news_list]  

    def get_list(self, db: Session, skip: int = 0, limit: int = 100) -> List[NewsSchema]:
        """✅ Retrieve a paginated list of news items."""
        news_list = db.query(News).offset(skip).limit(limit).all()
        return [NewsSchema.model_validate(news) for news in news_list]  

    def update(self, db: Session, news_id: int, obj_in: NewsUpdate) -> Optional[NewsSchema]:
        """✅ Update an existing news item."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None  
        for key, value in obj_in.model_dump(exclude_unset=True).items():
            setattr(db_news, key, value)
        db.commit()
        db.refresh(db_news)
        return NewsSchema.model_validate(db_news)  

    def remove(self, db: Session, news_id: int) -> Optional[NewsSchema]:
        """✅ Delete a news item, return None if already deleted."""
        db_news = db.query(News).filter(News.id == news_id).first()
        if not db_news:
            return None  
        db.delete(db_news)
        db.commit()
        return NewsSchema.model_validate(db_news)  

# ✅ Instance for proper importing
news_crud = NewsCRUD()