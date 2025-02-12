from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.endpoints.news import router as news_router
from src.api.endpoints.articles import router as articles_router  # ✅ Corrected import paths

app = FastAPI()

# ✅ Enable CORS to fix frontend connection issues
origins = [
    "http://127.0.0.1:3000",  # Allow frontend
    "http://localhost:3000"    # Just in case
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register API endpoints
app.include_router(news_router, prefix="/api")  # ✅ News routes
app.include_router(articles_router, prefix="/api")  # ✅ More specific than "fetch"
