from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.src.crud.news import news_crud  
from backend.src.database.db_connection import get_db
from backend.src.schemas.news import NewsCreate, NewsUpdate, News as NewsSchema

router = APIRouter()

@router.post("/", response_model=NewsSchema, status_code=201)
def create_news(news_data: NewsCreate, db: Session = Depends(get_db)):
    """✅ Creates a new news entry."""
    news = news_crud.create(db=db, obj_in=news_data)
    if not news:
        raise HTTPException(status_code=400, detail="Failed to create news")
    return news

@router.get("/", response_model=dict)
def get_all_news(db: Session = Depends(get_db)):
    """✅ Retrieves all news entries."""
    news_list = news_crud.get_all_news(db)
    return {"articles": news_list}  # ✅ Fix: Wrap response in `articles`

@router.get("/{news_id}", response_model=NewsSchema)
def get_news(news_id: int, db: Session = Depends(get_db)):
    """✅ Retrieves a single news entry by ID."""
    news_item = news_crud.get(db, news_id)
    if not news_item:
        raise HTTPException(status_code=404, detail="News item not found")
    return news_item

@router.put("/{news_id}", response_model=NewsSchema)
def update_news(news_id: int, news_update: NewsUpdate, db: Session = Depends(get_db)):
    """✅ Updates a news entry."""
    existing_news = news_crud.update(db, news_id, news_update)
    if not existing_news:
        raise HTTPException(status_code=404, detail="News item not found")
    return existing_news

@router.delete("/{news_id}", response_model=dict)
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """✅ Deletes a news entry."""
    deleted_news = news_crud.remove(db, news_id)
    if not deleted_news:
        raise HTTPException(status_code=404, detail="News item not found")
    return {"detail": "News item deleted successfully"}