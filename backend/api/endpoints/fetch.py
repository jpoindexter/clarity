from fastapi import APIRouter

router = APIRouter(prefix="/fetch", tags=["Fetch"])

@router.get("/rss", summary="Fetch and parse RSS feeds", description="Fetches articles from predefined RSS sources and parses them into the article database.")
async def fetch_rss():
    return {"message": "RSS fetch logic goes here."}