from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

# ✅ Import AI-powered functions
from backend.src.utils.ai_analysis import (
    detect_bias,
    score_credibility,
    find_contradictions,
    track_media_influence,
    fact_check_article
)

# ✅ Database & Models
from backend.src.database.db_connection import get_db
from backend.src.models.article import Article

# ✅ Schemas
from backend.src.schemas.article import Article as ArticleSchema, ArticleCreate

# ✅ Initialize Router
router = APIRouter(prefix="/articles", tags=["articles"])

# 🔹 **Retrieve All Articles**
@router.get("/", response_model=list[ArticleSchema])
def get_articles(db: Session = Depends(get_db)):
    """Retrieve all stored articles."""
    articles = db.query(Article).all()
    return articles if articles else []  # ✅ Returns an empty list instead of 404

# 🔹 **Create a New Article**
@router.post("/", response_model=ArticleSchema)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    """Create a new article entry."""
    new_article = Article(
        title=article.title,
        summary=article.summary,
        content=article.content,
        source=article.source,
        url=article.url,
        published_at=article.published_at or datetime.utcnow()
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

# 🔹 **Analyze an Article with AI**
@router.get("/analyze/{article_id}")
def analyze_article(article_id: int, db: Session = Depends(get_db)):
    """Perform AI-powered analysis on an article."""
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found.")

    return {
        "article_id": article_id,
        "title": article.title,
        "bias_analysis": detect_bias(article.content),
        "credibility_score": score_credibility(article.content),
        "fact_check": fact_check_article(article.content),
        "media_influence": track_media_influence(article.content),
        "contradictions": find_contradictions(article.content),
    }
