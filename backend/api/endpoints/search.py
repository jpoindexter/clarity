from fastapi import APIRouter, Query
from backend.schemas.news import NewsSchema
from backend.crud.news import news_crud

# ✅ Define the Router for this module (Prefix set here, not in `router.py`)
router = APIRouter(prefix="/api/search", tags=["search"])


@router.get("/", response_model=list[NewsSchema])
def fetch_news():
    """Fetch all news articles (should be in news, not search)."""
    return news_crud.get_news()


@router.get("/query", summary="Search for articles based on a query")
async def search_articles(q: str = Query(..., min_length=2, title="Search Query")):
    """
    Search for articles that match the given query.

    - **q**: Search keyword or phrase.
    """
    return {
        "query": q,
        "results": [
            {
                "id": 1,
                "title": "Placeholder Article",
                "summary": "This is a test article."
            },
            {"id": 2, "title": "Example News", "summary": "Another placeholder result."}
        ],
    }
