from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List 

from backend.schemas.content import ArticleCreate
from backend.schemas.article import SummarizedArticleRead
from backend.database import get_db

# --- Added as per instructions ---
from backend.models.article import Article
from backend.models.summarized_article import SummarizedArticle

def fetch_articles(db: Session):
    return db.query(SummarizedArticle).order_by(SummarizedArticle.id.desc()).limit(50).all()

def create_article(db: Session, article: ArticleCreate):
    new_article = Article(**article.model_dump())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

router = APIRouter() 

@router.get("/articles", response_model=List[SummarizedArticleRead])
def read_articles(db: Session = Depends(get_db)):
    articles = fetch_articles(db)
    return articles

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