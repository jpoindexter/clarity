<<<<<<< HEAD

# ✅ Ensure correct imports
from backend.api.endpoints.articles import router as articles_router
from backend.api.endpoints.news import router as news_router
from backend.api.endpoints.search import router as search_router
from backend.api.endpoints.contradiction import router as contradiction_router


# ✅ Register all routes
def include_routers(app):
    """Registers all API endpoints to the FastAPI app."""
    app.include_router(news_router, prefix="/api/news", tags=["news"])
    app.include_router(articles_router, prefix="/api/articles", tags=["articles"])
    app.include_router(search_router, prefix="/api/search", tags=["search"])
    app.include_router(
        contradiction_router,
        prefix="/api/contradictions",
        tags=["contradictions"]
    )
=======
from fastapi import APIRouter
from backend.api.endpoints.articles import router as articles_router
from backend.api.endpoints.news import router as news_router
from backend.api.endpoints.search import router as search_router
from backend.api.endpoints.contradictions import router as contradictions_router

router = APIRouter()

# ✅ Ensure proper route structure (Remove Duplicate `/api`)
router.include_router(news_router, prefix="", tags=["news"])
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
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
