# filepath: backend/src/api/endpoints/articles.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import TYPE_CHECKING

# ✅ Always import these at runtime to avoid missing module errors
from models.article import Article
from schemas.articles import ArticleCreate, Article as ArticleSchema
from database.db_connection import get_db

router = APIRouter()

@router.get("/api/articles", response_model=list[ArticleSchema], summary="Retrieve all articles")
def get_articles(db: Session = Depends(get_db)):
    """
    Retrieve a list of all articles from the database.
    """
    return db.query(Article).all()

@router.post("/api/articles", response_model=ArticleSchema, summary="Create a new article")
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    """
    Create a new article in the database.
    """
    new_article = Article(**article.model_dump())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
