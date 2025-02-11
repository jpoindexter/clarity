from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.crud.news import news as crud  # ✅ Correct
from src.database.db import get_db
from src.schemas import news as schemas

router = APIRouter()


@router.post("/api/news/", response_model=schemas.News)
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):
    """
    Create a new news item.
    """
    return crud.create_news(db=db, news=news)


@router.get("/api/news/{news_id}", response_model=schemas.News)
def read_news(news_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific news item by ID.
    """
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news


@router.get("/api/news/", response_model=List[schemas.News])
def read_news_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of news items.
    """
    news = crud.get_news_list(db, skip=skip, limit=limit)
    return news


@router.put("/api/news/{news_id}", response_model=schemas.News)
def update_news(news_id: int, news: schemas.NewsUpdate, db: Session = Depends(get_db)):
    """
    Update an existing news item.
    """
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return crud.update_news(db=db, news_id=news_id, news=news)


@router.delete("/api/news/{news_id}", response_model=schemas.News)
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """
    Delete a news item.
    """
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return crud.delete_news(db=db, news_id=news_id)
