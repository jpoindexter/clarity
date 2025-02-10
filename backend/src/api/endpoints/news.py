from fastapi import APIRouter

router = APIRouter()

@router.get("/news", tags=["news"])
def get_news():
    return {"news": ["Article 1", "Article 2", "Article 3"]}
