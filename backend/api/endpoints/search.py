from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from backend.crud.news import news_crud
from backend.database.db_connection import get_db
from backend.schemas.news import News as NewsSchema  # ✅ Ensuring correct schema import

# ✅ Define the Router for Search API
router = APIRouter(prefix="/api/search", tags=["search"])

# 🔹 **Fetch All News Articles (Moved Here)**


@router.get("/", response_model=list[NewsSchema])
def fetch_news(db: Session = Depends(get_db)):
    """Retrieve all stored news articles."""
    return news_crud.get_all(db)  # ✅ Uses `news_crud.get_all()`


# 🔹 **Search News Articles**
@router.get("/query", summary="Search for articles based on a query")
def search_articles(
    q: str = Query(..., min_length=2, title="Search Query"),
    db: Session = Depends(get_db)
):
    """
    Search for articles that match the given query.

    - **q**: Search keyword or phrase.
    """
    search_results = news_crud.search(db, q)  # ✅ Proper search handling
    return {
        "query": q,
        "results": search_results or []
    }  # ✅ Returns empty list if no results
