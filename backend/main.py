from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Enable CORS so the frontend (http://127.0.0.1:3000) can access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],  # Allow frontend to fetch data
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# ✅ Fake news data (temporary placeholder)
fake_news = [
    {"id": 1, "title": "Breaking: AI Advances Rapidly", "summary": "Researchers make a breakthrough in AI technology."},
    {"id": 2, "title": "Tech Industry Booming", "summary": "Stock prices for major tech companies are soaring."}
]

@app.get("/api/news/")
async def get_news():
    return fake_news
