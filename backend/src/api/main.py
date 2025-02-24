from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    """Lazy-loads the app to prevent circular imports"""

    app = FastAPI(
        title="Clairity API",
        description="AI-powered news aggregation and analysis platform",
        version="1.0",
    )

    # Enable CORS for frontend access
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


def include_routers(app):
    """Includes routers to the FastAPI application"""

    try:
        # ✅ Updated import paths to match new structure
        from backend.src.api.endpoints.articles import router as articles_router
        from backend.src.api.endpoints.news import router as news_router
        from backend.src.api.endpoints.search import router as search_router
        from backend.src.api.endpoints.contradiction import router as contradiction_router

        app.include_router(news_router, prefix="/api/v1/news", tags=["news"])
        app.include_router(
            articles_router, prefix="/api/v1/articles", tags=["articles"]
        )
        app.include_router(search_router, prefix="/api/v1/search", tags=["search"])
        app.include_router(
            contradiction_router, prefix="/api/v1/contradictions", tags=["contradictions"]
        )

    except ImportError as e:
        raise HTTPException(
            status_code=500, detail=f"🚨 Failed to import API routers: {str(e)}"
        ) from e  # ✅ Prevents silent errors

    return app


# ✅ Initialize the App
app = create_app()
include_routers(app)  # ✅ Ensure all routers are loaded


# ✅ Health Check Endpoint
@app.get("/", tags=["health"], summary="API Health Check")
def health_check():
    """Simple health check endpoint to verify API is running."""
    return {"status": "ok", "message": "🚀 Clairity API is running smoothly!"}
