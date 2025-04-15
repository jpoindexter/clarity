from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

# ✅ Import the contradiction detection service (ensure this function exists)
from backend.services.contradiction_detection import detect_contradictions


router = APIRouter(prefix="/contradiction", tags=["Contradiction"])


# Define Pydantic model for request validation
class Article(BaseModel):
    source: str
    headline: str
    content: str 


class ContradictionRequest(BaseModel):
    articles: List[Article]
  

@router.post(
    "/detect",
    summary="Run contradiction detection",
    description="Analyzes a list of news articles and returns contradiction signal classification between their claims."
)
async def detect_contradictions_endpoint(payload: ContradictionRequest):
    """
    API endpoint to detect contradictions between news articles.

    Example Request:
    {
        "articles": [
            {
                "source": "Reuters",
                "headline": "Stock market rises",
                "content": "The market increased today due to strong earnings."
            },
            {
                "source": "Bloomberg",
                "headline": "Stock market drops",
                "content": "The market fell today amid economic concerns."
            }
        ]
    }
    """
    if not payload.articles:
        raise HTTPException(
            status_code=400,
            detail="Articles list cannot be empty"
        )

    # Ensure structured data processing
    structured_articles = [article.dict() for article in payload.articles]

    contradictions = detect_contradictions(structured_articles)
    return contradictions
