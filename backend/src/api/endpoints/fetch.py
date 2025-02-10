from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import models, schemas
from api.deps import get_db

router = APIRouter()

@router.get("/api/news", summary="Retrieve the latest news")
def get_news(db: Session = Depends(get_db)):
    news = db.query(models.News).all()
    return news
