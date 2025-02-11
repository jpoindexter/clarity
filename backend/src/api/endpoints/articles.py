from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.article import Article  # ✅ Correct import for database models
from src.schemas.articles import ArticleCreate, Article  # ✅ Correct import for schemas
from src.database.db import get_db  # ✅ Fixed import

router = APIRouter()

@router.get("/api/articles", response_model=list[Article], summary="Retrieve all articles")
def get_articles(db: Session = Depends(get_db)):
    """
    Retrieve a list of all articles from the database.
    """
    return db.query(Article).all()

@router.post("/api/articles", response_model=Article, summary="Create a new article")
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    """
    Create a new article in the database.
    """
    new_article = Article(**article.dict())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
