<<<<<<< HEAD
# backend/src/api/endpoints/search.py
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/search", summary="Search for articles based on a query")
async def search_articles(q: str = Query(..., min_length=2, title="Search Query")):
    """
    Search for articles that match the given query.

    - **q**: Search keyword or phrase.
    """
    # ✅ Placeholder response until we implement `get_articles_by_query`
    return {
        "query": q,
        "results": [
            {"id": 1, "title": "Placeholder Article", "summary": "This is a test article."},
            {"id": 2, "title": "Example News", "summary": "Another placeholder result."}
        ],
    }
=======
from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.news import NewsSchema
from backend.crud.news import news_crud

# ✅ Define the Router for this module (Correct Prefix)
router = APIRouter(prefix="/search", tags=["search"])

# ✅ Define the route
@router.get("/", response_model=list[NewsSchema])
def fetch_news():
    return get_news()
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
