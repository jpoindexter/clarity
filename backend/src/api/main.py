from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoints.news import router as news_router  # ✅ Corrected import
from .endpoints.articles import router as articles_router  # ✅ Corrected import

app = FastAPI()

# ✅ Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],  # ✅ Allow frontend to fetch data
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods
    allow_headers=["*"],  # ✅ Allow all headers
)

# ✅ Register API endpoints
app.include_router(news_router, prefix="/api", tags=["news"])  # ✅ Ensures correct API structure
app.include_router(articles_router, prefix="/api", tags=["articles"])  # ✅ Ensures correct API structure
