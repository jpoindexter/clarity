from fastapi import FastAPI
api.endpoints.news import router as news_router
api.endpoints.articles import router as articles_router  # ✅ Updated import  # ✅ Add this

app = FastAPI()

app.include_router(news_router, prefix="/api")  # ✅ Ensures `/api/news/` works
app.include_router(articles_router, prefix="/api")  # ✅ Ensures `/api/articles/` works