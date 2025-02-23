from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# ✅ Database & Models
from backend.src.crud.news import news_crud
from backend.src.database.db_connection import get_db
from backend.src.models.news import News
# ✅ Schemas
from backend.src.schemas.news import News as NewsSchema
from backend.src.schemas.news import NewsCreate, NewsUpdate
# ✅ Import AI-powered misinformation detection
from backend.src.utils.ai_analysis import detect_misinformation

# ✅ Initialize Router
router = APIRouter(prefix="/news", tags=["news"])


# 🔹 **Analyze News for Misinformation**
@router.get("/analyze/{news_id}")
def analyze_news(news_id: int, db: Session = Depends(get_db)):
    """Analyze a news article for misinformation."""
    news_item = db.query(News).filter(News.id == news_id).first()
    if not news_item:
        raise HTTPException(status_code=404, detail="News item not found.")

    analysis_result = detect_misinformation(news_item.content)

    return {
        "news_id": news_id,
        "title": news_item.title,
        "source": news_item.source,
        "misinformation_analysis": analysis_result,
    }


# 🔹 **Retrieve All News Articles**
@router.get("/", response_model=list[NewsSchema])
def get_news(db: Session = Depends(get_db)):
    """Retrieve all stored news articles."""
    return news_crud.get_all(db)  # ✅ Calls `get_all()` from CRUD


# 🔹 **Retrieve a Single News Article**
@router.get("/{news_id}", response_model=NewsSchema)
def get_news_by_id(news_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific news article by ID."""
    news_item = news_crud.get(db, news_id)
    if not news_item:
        raise HTTPException(status_code=404, detail="News article not found.")
    return news_item


# 🔹 **Create a News Article**
@router.post("/", response_model=NewsSchema, status_code=201)
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    """Create a new news article entry."""
    if not all([news.title, news.content, news.source, news.url]):
        raise HTTPException(status_code=422, detail="Missing required fields.")

    return news_crud.create(db, obj_in=news)


# 🔹 **Update an Existing News Article**
@router.put("/{news_id}", response_model=NewsSchema)
def update_news(news_id: int, news: NewsUpdate, db: Session = Depends(get_db)):
    """Update an existing news article."""
    updated_news = news_crud.update(db, id=news_id, obj_in=news)
    if not updated_news:
        raise HTTPException(status_code=404, detail="News article not found.")
    return updated_news


# 🔹 **Delete a News Article**
@router.delete("/{news_id}", status_code=204)
def delete_news(news_id: int, db: Session = Depends(get_db)):
    """Delete a news article."""
    deleted_news = news_crud.remove(db, id=news_id)
    if not deleted_news:
        raise HTTPException(status_code=404, detail="News article not found.")
    return {"detail": "News article deleted successfully."}
