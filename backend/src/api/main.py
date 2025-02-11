from fastapi import FastAPI
from src.api.endpoints.news import router as news_router
from src.api.endpoints.articles import router as articles_router  # ✅ Updated import

app = FastAPI()

app.include_router(news_router, prefix="/api")  # ✅ News routes
app.include_router(articles_router, prefix="/api")  # ✅ More specific than "fetch"
