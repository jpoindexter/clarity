from fastapi import APIRouter
from backend.src.utils.fetch_module import fetch_news  # Adjust path if needed

router = APIRouter()

@router.get("/fetch", summary="Fetch the latest news articles")
async def fetch_articles():
    """
    Fetch the latest news articles from RSS sources and return them.
    """
    articles = fetch_news()
    return {"articles": articles}
