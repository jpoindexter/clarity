# ✅ Ensure correct imports
from fastapi import APIRouter
from backend.api.endpoints.articles import router as articles_router
from backend.api.endpoints.news import router as news_router
from backend.api.endpoints.search import router as search_router
from backend.api.endpoints.contradiction import router as contradiction_router

# ✅ Create a main router
router = APIRouter()

# ✅ Register all routes
router.include_router(news_router, prefix="/news", tags=["news"])
router.include_router(articles_router, prefix="/articles", tags=["articles"])
router.include_router(search_router, prefix="/search", tags=["search"])
router.include_router(
    contradiction_router, prefix="/contradictions", tags=["contradictions"]
)


# ✅ Function to include routers in the FastAPI app
def include_routers(app):
    """Registers all API endpoints to the FastAPI app."""
    app.include_router(router)
