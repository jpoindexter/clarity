from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.db_connection import get_db
from backend.src.models.article import Article
from backend.src.schemas.content import Article as ArticleSchema
from backend.src.schemas.content import ArticleCreate

router = APIRouter(prefix="", tags=["articles"])


@router.get("/", response_model=list[ArticleSchema], summary="Retrieve all articles")
def get_articles(db: Session = Depends(get_db)):
    return db.query(Article).all()


@router.post("/", response_model=ArticleSchema, summary="Create a new article")
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    new_article = Article(**article.model_dump())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
