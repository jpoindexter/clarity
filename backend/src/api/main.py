from fastapi import FastAPI
from api.endpoints.news import router as news_router

app = FastAPI()

app.include_router(news_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "FastAPI backend is running!"}
