from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.news import NewsSchema
from backend.crud.news import news_crud
from backend.database import get_db  # ✅ Corrected import

router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("/", response_model=list[NewsSchema])
def fetch_news(db: Session = Depends(get_db)):  # ✅ Inject DB dependency
    return news_crud.get_news(db)
