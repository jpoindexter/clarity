"""
CRUD operations for articles.
"""

from sqlalchemy.orm import Session

from backend.models.article import Article  # ✅ Ensure correct import
from backend.schemas.content import ArticleCreate  # ✅ Schema import


def fetch_articles(db: Session):
    """Retrieve all articles from the database."""
    return db.query(Article).all()


def create_article(db: Session, article_data: ArticleCreate):
    """Create a new article in the database."""
    new_article = Article(
        **article_data.model_dump()
    )  # ✅ Convert Pydantic model to dict
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

from backend.schemas.article import SummarizedArticleCreate
from backend.models import SummarizedArticle

def save_summarized_article(db: Session, article_data: SummarizedArticleCreate):
    """Save summarized article content to the database after AI processing."""
    new_summary = SummarizedArticle(**article_data.model_dump())
    db.add(new_summary)
    db.commit()
    db.refresh(new_summary)
    return new_summary
   