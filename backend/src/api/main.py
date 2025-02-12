from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints.news import router as news_router
from api.endpoints.articles import router as articles_router

app = FastAPI()

# ✅ Fix: Explicitly set allowed origins & debug CORS errors
origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # ✅ Only allow necessary methods
    allow_headers=["*"],
)

# ✅ Register API endpoints
app.include_router(news_router, prefix="/api", tags=["news"])
app.include_router(articles_router, prefix="/api", tags=["articles"])

# ✅ Debugging CORS Errors (Optional: You can remove this later)
@app.get("/test-cors")
def test_cors():
    return {"message": "CORS is working!"}
