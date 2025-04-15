from fastapi import APIRouter
from datetime import datetime
from typing import List

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])

@router.get(
    "/summary",
    summary="Get summary stats for the intelligence dashboard",
    description="Returns basic counts and metadata for the dashboard, including total and flagged articles, and top sources.",
)
def get_dashboard_summary():
    # Placeholder logic — replace with real DB queries
    return {
        "total_articles": 124,
        "flagged_articles": 17,
        "last_updated": datetime.utcnow().isoformat(),
        "top_sources": ["Reuters", "BBC", "NYT"]
    }
