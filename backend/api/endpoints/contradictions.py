from fastapi import APIRouter

router = APIRouter(prefix="/api/contradictions", tags=["contradictions"])


@router.post(
    "/detect",
    summary="Run contradiction detection",
    description="Analyzes a list of news articles and returns contradiction signal classification between their claims."
)
def detect_contradictions():
    return {"message": "Detecting contradictions..."}