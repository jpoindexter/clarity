from fastapi import APIRouter, HTTPException
from typing import List, Dict

# ✅ Import the contradiction detection service (ensure this function exists)
from backend.src.services.contradiction_detection import detect_contradictions

router = APIRouter()


@router.post("/detect")
async def detect_contradictions_endpoint(payload: Dict):
    """
    API endpoint to detect contradictions between news articles.

    Example Request:
    {
        "articles": [
            {"source": "Reuters", "headline": "Stock market rises", "content": "The market increased today due to strong earnings."},
            {"source": "Bloomberg", "headline": "Stock market drops", "content": "The market fell today amid economic concerns."}
        ]
    }
    """
    if "articles" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'articles' field")

    contradictions = detect_contradictions(payload["articles"])
    return {"contradictions": contradictions}
