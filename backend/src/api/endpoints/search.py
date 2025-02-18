from fastapi import APIRouter, Query
from backend.src.models.article import Article  # Ensure this import is correct
from backend.src.utils.db_helper import get_articles_by_query  # Ensure this import is correct

router = APIRouter()

@router.get("/search", summary="Search for articles based on a query")
async def search_articles(q: str = Query(..., min_length=2, title="Search Query")):
    """
    Search for articles that match the given query.

    - **q**: Search keyword or phrase.
    """
    results = get_articles_by_query(q)
    return {"query": q, "results": results}
