from fastapi import FastAPI
from backend.src.api.endpoints.news import router as news_router
from backend.src.api.endpoints.articles import router as articles_router  # ✅ Correct import

app = FastAPI()

app.include_router(news_router, prefix="/api")  # ✅ Ensures `/api/news/` works
app.include_router(articles_router, prefix="")  # ✅ Fixes `/api/api/articles` issue
