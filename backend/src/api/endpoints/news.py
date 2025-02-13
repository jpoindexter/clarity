from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text  # ✅ Import text() for raw SQL queries

from src.crud.news import news as crud  # ✅ Adjusted import path for CRUD functions
from src.database.db_connection import get_db  # ✅ Correct database session import
from src.schemas.news import NewsCreate, NewsUpdate, News  # ✅ Fixed schema import paths

router = APIRouter(prefix="/news", tags=["news"])  # ✅ Ensure correct API route prefix

@router.post("/", response_model=News, summary="Create a news article")
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    """Create a new news item."""
    try:
        new_news = crud.create_news(db=db, news=news)
        print(f"✅ Created News: {new_news}")
        return new_news
    except SQLAlchemyError as e:
        print(f"❌ Error creating news: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/{news_id}", response_model=News, summary="Retrieve a specific news article")
def read_news(news_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific news item by ID."""
    try:
        db_news = crud.get_news(db, news_id=news_id)
        if db_news is None:
            print(f"⚠️ News ID {news_id} not found.")
            raise HTTPException(status_code=404, detail="News not found")
        print(f"✅ Fetched News ID {news_id}: {db_news}")
        return db_news
    except SQLAlchemyError as e:
        print(f"❌ Error fetching news: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@router.get("/", response_model=List[News], summary="Retrieve a list of news articles")
def read_news_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve a list of news items."""

    # 🔍 Debug: Run raw SQL query first
    try:
        raw_sql_check = db.execute(text("SELECT * FROM news")).fetchall()  # ✅ Fixed text() issue
        print(f"🔍 Raw SQL Query Result: {raw_sql_check}")
    except SQLAlchemyError as e:
        print(f"❌ Error running raw SQL: {e}")
        raise HTTPException(status_code=500, detail="Database error in raw SQL check")

    # ✅ Check ORM Query
    try:
        news_list = crud.get_news_list(db, skip=skip, limit=limit)
        print(f"✅ ORM Query Result: {news_list}")
        return news_list
    except SQLAlchemyError as e:
        print(f"❌ Error fetching news list: {e}")
        raise HTTPException(status_code=500, detail="Database error in fetching news list")

@router.put("/{news_id}", response_model=News, summary="Update an existing news article")
def NewsUpdate(news_id: int, news: NewsUpdate, db: Session = Depends(get_db)):
    """Update an existing news item."""
    try:
        db_news = crud.get_news(db, news_id=news_id)
        if db_news is None:
            print(f"⚠️ News ID {news_id} not found.")
            raise HTTPException(status_code=404, detail="News not found")
        
        updated_news = crud.NewsUpdate(db=db, news_id=news_id, news=news)
        print(f"✅ Updated News ID {news_id}: {updated_news}")
        return updated_news
    except SQLAlchemyError as e:
        print(f"❌ Error updating news: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@router.delete("/{news_id}", response_model=News, summary="Delete a news article")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """Delete a news item."""
    try:
        db_news = crud.get_news(db, news_id=news_id)
        if db_news is None:
            print(f"⚠️ News ID {news_id} not found.")
            raise HTTPException(status_code=404, detail="News not found")
        
        deleted_news = crud.delete_news(db=db, news_id=news_id)
        print(f"✅ Deleted News ID {news_id}: {deleted_news}")
        return deleted_news
    except SQLAlchemyError as e:
        print(f"❌ Error deleting news: {e}")
        raise HTTPException(status_code=500, detail="Database error")
