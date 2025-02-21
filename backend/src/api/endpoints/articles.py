from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from backend.src.database.db_connection import get_db
from backend.src.models.article import Article
from backend.src.schemas.content import Article as ArticleSchema
from backend.src.schemas.content import ArticleCreate

router = APIRouter(prefix="/articles", tags=["articles"])

@router.get("/", response_model=list[ArticleSchema], summary="Retrieve all articles")
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    
    if not articles:
        raise HTTPException(status_code=404, detail="No articles found")
        
    return articles

@router.post("/", response_model=ArticleCreate)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    new_article = Article(
        title=article.title,
        summary=article.summary,
        content=article.content,
        source=article.source,
        url=article.url,
        published_at=article.published_at or datetime()
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
