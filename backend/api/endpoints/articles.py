from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from backend.database.db_connection import get_db
from backend.models.article import SummarizedArticle

router = APIRouter(prefix="/articles", tags=["Articles"])
@router.get(
    "/",
    response_model=dict[str, list[dict]],
    summary="Search summarized articles",
    description="Returns a list of summarized articles filtered by optional query, tone, or source, with pagination."
) 
def get_articles(
    db: Session = Depends(get_db),
    query: Optional[str] = None,
    tone: Optional[str] = None,
    source: Optional[str] = None,
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    """
    Retrieve summarized articles with optional filters and pagination.

    Args:
        db (Session): Database session.
        query (str, optional): Text query to search in title or summary.
        tone (str, optional): Tone filter.
        source (str, optional): Source filter.
        limit (int): Max results to return.
        offset (int): Number of results to skip.

    Returns:
        dict: {"articles": List of article dicts}
    """
    q = db.query(SummarizedArticle).filter(SummarizedArticle.summary.isnot(None))

    if query:
        search = f"%{query.lower()}%"
        q = q.filter(
            SummarizedArticle.title.ilike(search) |
            SummarizedArticle.summary.ilike(search)
        )

    if tone:
        q = q.filter(SummarizedArticle.tone == tone)

    if source:
        q = q.filter(SummarizedArticle.source == source)

    total_count = q.count()

    articles = q.order_by(SummarizedArticle.timestamp.desc()).offset(offset).limit(limit).all()

    return {
        "articles": [
            {
                "title": a.title,
                "summary": a.summary,
                "date": a.timestamp,
                "source": a.source,
                "tone": a.tone,
                "manipulation_risk": a.manipulation_risk
            }
            for a in articles
        ],
        "total_count": total_count
    } 