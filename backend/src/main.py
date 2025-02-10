from fastapi import FastAPI
from src.api.endpoints.news import router as news_router

app = FastAPI()
app.include_router(news.router, prefix="/api")
