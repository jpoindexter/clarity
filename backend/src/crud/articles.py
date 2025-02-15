"""
CRUD operations for articles.
"""

from sqlalchemy.orm import Session
from backend.src.models.article import Article  # ✅ Ensure correct import
from backend.src.schemas.content import ArticleCreate  # ✅ Schema import


def fetch_articles(db: Session):
    """Retrieve all articles from the database."""
    return db.query(Article).all()


def create_article(db: Session, article_data: ArticleCreate):
    """Create a new article in the database."""
    new_article = Article(**article_data.model_dump())  # ✅ Convert Pydantic model to dict
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article