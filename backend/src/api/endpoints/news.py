from typing import Optional
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.src.crud.news import news_crud
from backend.src.database.db_connection import get_db
from backend.src.schemas.news import News as NewsSchema, NewsCreate, NewsUpdate

router = APIRouter()


@router.post("/", response_model=NewsCreate)
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    new_news = news(
        title=news.title,
        content=news.content,
        source=news.source,
        url=news.url,
        created_at=news.created_at or datetime()
    )
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return new_news


@router.get("/", response_model=list[NewsSchema])
def get_all_news(db: Session = Depends(get_db)):
    """✅ Retrieves all news entries."""
    return news_crud.get_all_news(db)  # ✅ Now directly returns serialized objects


@router.get("/{news_id}", response_model=NewsSchema)
def get_news(news_id: int, db: Session = Depends(get_db)):
    """✅ Retrieves a single news entry by ID."""
    news_item = news_crud.get(db, news_id)
    if not news_item:
        raise HTTPException(status_code=404, detail="News item not found")
    return news_item


@router.put("/{news_id}", response_model=NewsSchema)
def update_news(
    news_id: int,
    update_data: NewsUpdate,
    db: Session = Depends(get_db),
):
    """✅ Update an existing news item."""
    existing_news = news_crud.get(db, news_id)

    if not existing_news:
        raise HTTPException(status_code=404, detail="News item not found")

    updated_news = news_crud.update(db, db_obj=existing_news, obj_in=update_data)
    return updated_news


@router.delete("/{news_id}", response_model=dict)
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """✅ Deletes a news entry."""
    deleted_news = news_crud.remove(db, news_id)
    if not deleted_news:
        raise HTTPException(status_code=404, detail="News item not found")
    return {"detail": "News item deleted successfully"}