from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# ✅ Database & Models
from backend.src.database.db_connection import get_db
from backend.src.models.news import News
# ✅ Schemas
from backend.src.schemas.news import News as NewsSchema
from backend.src.schemas.news import NewsCreate

# ✅ Initialize Router
router = APIRouter(prefix="/news", tags=["news"])


# 🔹 **Retrieve All News**
@router.get("/", response_model=list[NewsSchema])
def get_news(db: Session = Depends(get_db)):
    """Retrieve all stored news articles."""
    news_articles = db.query(News).all()
    return news_articles if news_articles else []  # ✅ Returns an empty list instead of 404


# 🔹 **Create a New News Entry**
@router.post("/", response_model=NewsSchema)
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    """Create a new news entry."""
    new_news = News(
        title=news.title,
        summary=news.summary,
        content=news.content,
        source=news.source,
        url=news.url,
        published_at=news.published_at or datetime.utcnow(),
    )
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return new_news