from fastapi import FastAPI
from src.api.endpoints.news import router as news_router  # ✅ Correct import

app = FastAPI()
app.include_router(news_router, prefix="/api")  # ✅ Use `news_router` instead

