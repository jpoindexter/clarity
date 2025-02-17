from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.src.crud.news import news_crud  
from backend.src.database.db_connection import get_db
from backend.src.schemas.news import NewsCreate, NewsUpdate, News as NewsSchema
from typing import Optional

router = APIRouter()

# ✅ Create News Entry
@router.post("/", response_model=NewsSchema, status_code=201)
def create_news(news_data: NewsCreate, db: Session = Depends(get_db)):
    """✅ Creates a new news entry."""
    news = news_crud.create(db=db, obj_in=news_data)
    if not news:
        raise HTTPException(status_code=400, detail="Failed to create news")
    return news

# ✅ Get All News
@router.get("/", response_model=dict)
def get_all_news(db: Session = Depends(get_db)):
    """✅ Retrieves all news entries."""
    news_list = news_crud.get_all_news(db)
    return {"articles": news_list}

# ✅ Get Single News by ID
@router.get("/{news_id}", response_model=NewsSchema)
def get_news(news_id: int, db: Session = Depends(get_db)):
    """✅ Retrieves a single news entry by ID."""
    news_item = news_crud.get(db, news_id)
    if not news_item:
        raise HTTPException(status_code=404, detail="News item not found")
    return news_item

# ✅ **Fix: Ensure 404 is checked BEFORE validation**
@router.put("/{news_id}", response_model=NewsSchema)
def update_news(
    news_id: int, 
    title: Optional[str] = None, 
    content: Optional[str] = None, 
    source: Optional[str] = None, 
    url: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    """✅ Update an existing news item"""
    existing_news = news_crud.get(db, news_id)  # ✅ Fetch the news item **first**

    if not existing_news:
        raise HTTPException(status_code=404, detail="News item not found")  # ✅ Ensure 404 comes before validation

    # ✅ Prevent empty updates
    if not any([title, content, source, url]):  
        raise HTTPException(status_code=422, detail="Update payload cannot be empty")  

    update_data = {
        "title": title or existing_news.title,
        "content": content or existing_news.content,
        "source": source or existing_news.source,
        "url": url or existing_news.url
    }

    updated_news = news_crud.update(db, db_obj=existing_news, obj_in=update_data)
    return updated_news

# ✅ Delete News Entry
@router.delete("/{news_id}", response_model=dict)
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """✅ Deletes a news entry."""
    deleted_news = news_crud.remove(db, news_id)
    if not deleted_news:
        raise HTTPException(status_code=404, detail="News item not found")
    return {"detail": "News item deleted successfully"}