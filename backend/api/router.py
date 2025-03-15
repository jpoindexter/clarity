from fastapi import APIRouter

# ✅ Import Endpoints
from backend.api.endpoints.news import router as news_router
from backend.api.endpoints.search import router as search_router

# ✅ Initialize main API router
router = APIRouter()

# ✅ Include News API Routes
router.include_router(news_router)  # ✅ `prefix="/api/news"` is handled in news.py

# ✅ Include Search API Routes
router.include_router(search_router)  # ✅ `prefix="/api/search"` is handled in search.py
