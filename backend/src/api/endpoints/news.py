from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.crud.news import news as crud  # ✅ Correct import for database interactions
from src.database.db_connection import get_db  # ✅ Corrected import for database session
from src.schemas.news import NewsCreate, NewsUpdate, News  # ✅ Correct import for schemas

router = APIRouter(prefix="/news", tags=["news"])  # ✅ Fix: Ensures correct API path

@router.post("/", response_model=News)
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    """
    Create a new news item.
    """
    return crud.create_news(db=db, news=news)

@router.get("/{news_id}", response_model=News)
def read_news(news_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific news item by ID.
    """
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news

@router.get("/", response_model=List[News])
def read_news_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of news items.
    """
    news = crud.get_news_list(db, skip=skip, limit=limit)
    return news

@router.put("/{news_id}", response_model=News)
def update_news(news_id: int, news: NewsUpdate, db: Session = Depends(get_db)):
    """
    Update an existing news item.
    """
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return crud.update_news(db=db, news_id=news_id, news=news)

@router.delete("/{news_id}", response_model=News)
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """
    Delete a news item.
    """
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return crud.delete_news(db=db, news_id=news_id)
