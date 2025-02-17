from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ Import API routers with strict error handling
try:
    from backend.src.api.endpoints.news import router as news_router
    from backend.src.api.endpoints.articles import router as articles_router
except ImportError as e:
    raise RuntimeError(f"❌ ERROR: Failed to import API routers - {e}") from e  # ✅ Throw an error instead of failing silently

# ✅ Initialize FastAPI app
app = FastAPI(
    title="Clairity API",
    description="🚀 AI-powered news aggregation and analysis platform",
    version="1.0"
)

# ✅ Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],  # ✅ Allow frontend to fetch data
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods
    allow_headers=["*"],  # ✅ Allow all headers
)

# ✅ Register API endpoints
app.include_router(news_router, prefix="/api/v1/news", tags=["news"])
app.include_router(articles_router, prefix="/api/v1/articles", tags=["articles"])

# ✅ Health Check Endpoint
@app.get("/", tags=["health"], summary="API Health Check")
def health_check():
    """Simple health check endpoint to verify API is running."""
    return {"status": "ok", "message": "Clairity API is running smoothly 🚀"}

# ✅ Print registered routes correctly
import inspect
print("✅ Registered Routes:", [route.path for route in app.routes])
