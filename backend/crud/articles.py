import json
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List 

from backend.schemas.content import ArticleCreate
from backend.schemas.article import SummarizedArticleRead
from backend.database import get_db

# --- Added as per instructions ---
from backend.models.article import Article
from backend.models.article import SummarizedArticle
  
def fetch_articles(db: Session, tag: List[str] = None, tone: str = None, source: str = None):
    query = db.query(SummarizedArticle).filter(SummarizedArticle.summary.isnot(None))
 
    if tone:
        query = query.filter(SummarizedArticle.tone == tone)
    if source:
        query = query.filter(SummarizedArticle.source == source)
    if tag:
        for t in tag:
            # Normalize tag: remove quotes and lowercase for matching
            norm_t = t.strip(' "\'').lower()
            # Use JSONB containment operator to filter by tags
            query = query.filter(SummarizedArticle.tags.op('@>')(json.dumps([norm_t])))

    articles = query.order_by(SummarizedArticle.timestamp.desc()).limit(100).all()

    result = []
    for article in articles:
        if isinstance(article.tags, str):
            try:
                article.tags = json.loads(article.tags)
                if not isinstance(article.tags, list):
                    article.tags = []
            except Exception as e:
                print("JSON decode error:", e)
                article.tags = []

        if not hasattr(article, "published_at") or article.published_at is None:
            article.published_at = getattr(article, "timestamp", datetime.utcnow())

        result.append(SummarizedArticleRead.model_validate(article))

    return result

def create_article(db: Session, article: ArticleCreate):
    new_article = Article(**article.model_dump())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article   

router = APIRouter()   

@router.get("/articles", response_model=List[SummarizedArticleRead])
def read_articles(db: Session = Depends(get_db)):
    return fetch_articles(db)
 
@router.post("/articles", response_model=SummarizedArticleRead)
def add_article(article: ArticleCreate, db: Session = Depends(get_db)):
    new_article = create_article(db, article)
    return new_article  


# Restore save_summarized_article to support saving AI-generated summaries.
from backend.schemas.article import SummarizedArticleCreate

def save_summarized_article(db: Session, article_data: SummarizedArticleCreate):
    new_summary = SummarizedArticle(**article_data.model_dump())
    db.add(new_summary)
    db.commit()
    db.refresh(new_summary)
    return new_summary 