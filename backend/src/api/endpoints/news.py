"""
API Endpoints for managing news data.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.src.crud.news import news_crud  # ✅ Fixing incorrect import
from backend.src.database.db_connection import get_db
from backend.src.schemas.news import NewsCreate, NewsUpdate, News as NewsSchema

router = APIRouter()

@router.post("/", response_model=NewsSchema)
def create_news(news_data: NewsCreate, db: Session = Depends(get_db)):
    """
    Creates a new news entry.
    """
    try:
        return news_crud.create(db=db, obj_in=news_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error") from e

@router.get("/{news_id}", response_model=NewsSchema)
def get_news(news_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a news entry by ID.
    """
    news_item = news_crud.get(db, id=news_id)
    if not news_item:
        raise HTTPException(status_code=404, detail="News item not found")
    return news_item

@router.put("/{news_id}", response_model=NewsSchema)
def update_news(news_id: int, news_update: NewsUpdate, db: Session = Depends(get_db)):
    """
    Updates a news entry.
    """
    existing_news = news_crud.get(db, id=news_id)
    if not existing_news:
        raise HTTPException(status_code=404, detail="News item not found")
    
    try:
        return news_crud.update(db=db, db_obj=existing_news, obj_in=news_update)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error") from e

@router.delete("/{news_id}")
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """
    Deletes a news entry.
    """
    existing_news = news_crud.get(db, id=news_id)
    if not existing_news:
        raise HTTPException(status_code=404, detail="News item not found")
    
    try:
        news_crud.remove(db=db, id=news_id)
        return {"detail": "News item deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error") from e
