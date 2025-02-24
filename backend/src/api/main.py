from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging


# ✅ Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    """Lazy-loads the app to prevent circular imports"""
    app = FastAPI(
        title="Clairity API",
        description="AI-powered intelligence and analysis platform",
        version="1.0",
    )

    # ✅ Enable CORS for frontend access
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://127.0.0.1:3000",
            "http://localhost:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


def include_routers(app):
    """Includes routers to the FastAPI application"""
    try:
        # ✅ Updated import paths (ensuring correct module resolution)
        from backend.src.api.endpoints.articles import router as articles_router
        from backend.src.api.endpoints.news import router as news_router
        from backend.src.api.endpoints.search import router as search_router
        from backend.src.api.endpoints.contradiction import (
            router as contradiction_router,
        )

        # ✅ Include API routers
        app.include_router(news_router, prefix="/api/v1/news", tags=["news"])
        app.include_router(articles_router, prefix="/api/v1/articles", tags=["articles"])  # noqa: E501
        app.include_router(search_router, prefix="/api/v1/search", tags=["search"])  # noqa: E501
        app.include_router(
            contradiction_router, prefix="/api/v1/contradictions", tags=["contradictions"]  # noqa: E501
        )

    except ImportError as e:
        logger.error(f"🚨 Failed to import API routers: {e}")
        raise RuntimeError(f"🚨 Router Import Error: {str(e)}") from e

    return app


# ✅ Initialize the App & Load Routers
app = create_app()
include_routers(app)


# ✅ Health Check Endpoint
@app.get("/", tags=["health"], summary="API Health Check")
def health_check():
    """Simple health check endpoint to verify API is running."""
    return {"status": "ok", "message": "🚀 Clairity API is running smoothly!"}
