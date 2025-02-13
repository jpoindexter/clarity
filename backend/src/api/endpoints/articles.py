# filepath: backend/src/api/endpoints/articles.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.article import Article  # ✅ Corrected import path
from src.schemas.content import ArticleCreate, Article as ArticleSchema  # ✅ Fixed schema path
from src.database.db_connection import get_db  # ✅ Fixed database session import

router = APIRouter(prefix="/articles", tags=["articles"])  # ✅ Added `prefix="/articles"` for proper API structure

@router.get("/", response_model=list[ArticleSchema], summary="Retrieve all articles")
def get_articles(db: Session = Depends(get_db)):
    """
    Retrieve a list of all articles from the database.
    """
    return db.query(Article).all()

@router.post("/", response_model=ArticleSchema, summary="Create a new article")
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    """
    Create a new article in the database.
    """
    new_article = Article(**article.model_dump())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
