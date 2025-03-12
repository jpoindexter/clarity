from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.news import NewsSchema
from backend.crud.news import news_crud

# ✅ Define the Router for this module (Correct Prefix)
router = APIRouter(prefix="/search", tags=["search"])

# ✅ Define the route
@router.get("/", response_model=list[NewsSchema])
def fetch_news():
    return get_news()
