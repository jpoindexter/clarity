from fastapi import APIRouter

# ✅ Import Endpoints
from backend.api.endpoints.news import router as news_router
from backend.api.endpoints.search import router as search_router

# ✅ Initialize main API router
router = APIRouter()

# ✅ Include News API Routes (Prefix is already set in `news.py`)
router.include_router(news_router)

# ✅ Include Search API Routes (Prefix is already set in `search.py`)
router.include_router(search_router)
