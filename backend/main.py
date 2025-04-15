from fastapi import FastAPI
from backend.api.endpoints import (
    summarize,
    news,
    articles,
    analyze,
    fetch,
    search
)

# ✅ Initialize FastAPI application
app = FastAPI(title="Clarity AI")

# ✅ Include all API routes
app.include_router(summarize.router)
app.include_router(news.router)
app.include_router(articles.router)
app.include_router(analyze.router)
app.include_router(fetch.router)
app.include_router(search.router)
 
 
# ✅ Root route for testing
@app.get("/")
def root():
    return {"message": "Welcome to Clarity AI"} 


# ✅ Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
