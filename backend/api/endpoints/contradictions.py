from fastapi import APIRouter

router = APIRouter(prefix="/api/contradictions", tags=["contradictions"])


@router.post("/detect")
def detect_contradictions():
    return {"message": "Detecting contradictions..."}
