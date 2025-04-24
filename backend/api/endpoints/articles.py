from fastapi import APIRouter
from backend.utils.article_fetcher import fetch_articles  # Utility function for fetching articles from RSS
from backend.schemas.schemas import SummarizedArticleCreate  # Import the SummarizedArticleCreate schema
from typing import List

router = APIRouter()

@router.get("/articles", response_model=List[SummarizedArticleCreate])
async def get_articles(query: str):
    # Fetch articles from Google News RSS
    articles = fetch_articles(query)
    return articles 