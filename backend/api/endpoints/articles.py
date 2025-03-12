from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.news import NewsSchema
from backend.crud.news import get_news

# ✅ Define the Router for this module (Correct Prefix)
router = APIRouter(prefix="/articles", tags=["articles"])

# ✅ Define the route
@router.get("/", response_model=list[NewsSchema])
def fetch_news():
    return get_news()

from backend.crud.news import news_crud  # Ensure correct import
