from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.crud.news import news as crud  # ✅ Adjusted import path for CRUD functions
from src.database.db_connection import get_db  # ✅ Correct database session import
from src.schemas.news import NewsCreate, NewsUpdate, News  # ✅ Fixed schema import paths

router = APIRouter(prefix="/news", tags=["news"])  # ✅ Ensure correct API route prefix

@router.post("/", response_model=News, summary="Create a news article")
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    """Create a new news item."""
    return crud.create_news(db=db, news=news)

@router.get("/{news_id}", response_model=News, summary="Retrieve a specific news article")
def read_news(news_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific news item by ID."""
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news

@router.get("/", response_model=List[News], summary="Retrieve a list of news articles")
def read_news_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve a list of news items."""
    return crud.get_news_list(db, skip=skip, limit=limit)

@router.put("/{news_id}", response_model=News, summary="Update an existing news article")
def update_news(news_id: int, news: NewsUpdate, db: Session = Depends(get_db)):
    """Update an existing news item."""
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return crud.update_news(db=db, news_id=news_id, news=news)

@router.delete("/{news_id}", response_model=News, summary="Delete a news article")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """Delete a news item."""
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return crud.delete_news(db=db, news_id=news_id)
