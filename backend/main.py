from fastapi import FastAPI

app = FastAPI()

# Sample News Data
fake_news = [
    {"id": 1, "title": "Breaking: AI Advances Rapidly", "summary": "Researchers make a breakthrough in AI technology."},
    {"id": 2, "title": "Tech Industry Booming", "summary": "Stock prices for major tech companies are soaring."}
]

@app.get("/api/api/news/")
async def get_news():
    return fake_news
