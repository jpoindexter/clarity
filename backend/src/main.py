from fastapi import FastAPI
from api.endpoints.news import router as news_router

app = FastAPI()
app.include_router(news.router, prefix="/api")
