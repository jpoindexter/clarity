from fastapi import APIRouter
from backend.api.endpoints.articles import router as articles_router
from backend.api.endpoints.news import router as news_router
from backend.api.endpoints.search import router as search_router
from backend.api.endpoints.contradictions import router as contradiction_router

router = APIRouter()

# ✅ Fix duplicate prefix issue
router.include_router(news_router, prefix="/api/news", tags=["news"])
router.include_router(articles_router, prefix="/api/articles", tags=["articles"])
router.include_router(search_router, prefix="/api/search", tags=["search"])
router.include_router(
    contradiction_router, prefix="/api/contradictions", tags=["contradictions"]
)

router.include_router(news_router, prefix='/api/news', tags=['news'])
