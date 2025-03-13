<<<<<<< HEAD
from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# ✅ Database & Models
from backend.database.db_connection import get_db
from backend.models.article import Article  # ✅ Using Article model

# ✅ Schemas
from backend.schemas.article import Article as ArticleSchema
from backend.schemas.article import ArticleCreate  # ✅ Correct Schema

# ✅ Initialize Router (REMOVE the prefix here)
router = APIRouter(
    tags=["articles"],
)

# 🔹 **Retrieve All Articles**


@router.get("/", response_model=list[ArticleSchema])
def get_articles(db: Session = Depends(get_db)):
    """
    Retrieve all stored articles.

    Returns:
        list[ArticleSchema]: List of stored articles.
        If no articles exist, returns an empty list.
    """
    articles = db.query(Article).all()
    return articles if articles else []  # ✅ Returns an empty list instead of 404

# 🔹 **Create a New Article Entry**


@router.post("/", response_model=ArticleSchema)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    """
    Create a new article entry.

    Args:
        article (ArticleCreate): Data for the new article.
        db (Session): Database session.

    Returns:
        ArticleSchema: The created article.
    """
    new_article = Article(
        title=article.title,
        summary=article.summary,
        content=article.content,
        source=article.source,
        url=article.url,
        published_at=article.published_at or datetime.utcnow(),
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
=======
from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.news import NewsSchema
from backend.crud.news import news_crud

# ✅ Define the Router for this module (Correct Prefix)
router = APIRouter(prefix="/articles", tags=["articles"])

# ✅ Define the route
@router.get("/", response_model=list[NewsSchema])
def fetch_news():
    return get_news()

from backend.crud.news import news_crud  # Ensure correct import
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
