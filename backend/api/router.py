from fastapi import APIRouter
from backend.api.endpoints.articles import router as articles_router
from backend.api.endpoints.news import router as news_router
from backend.api.endpoints.search import router as search_router
from backend.api.endpoints.contradictions import router as contradictions_router

router = APIRouter()

# ✅ Ensure proper route structure (Remove Duplicate `/api`)
router.include_router(news_router, prefix="/api/news", tags=["news"])
router.include_router(articles_router, prefix="/api/articles", tags=["articles"])
router.include_router(search_router, prefix="/api/search", tags=["search"])
router.include_router(
    contradictions_router,
    prefix="/api/contradictions",
    tags=["contradictions"]
)


def include_routers(app):
    """Ensure all routes are included correctly."""
    app.include_router(router)
