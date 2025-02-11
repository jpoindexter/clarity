from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
import datetime
from typing import TYPE_CHECKING

Base = declarative_base()

if TYPE_CHECKING:
    from schemas.articles import ArticleSchema  # Forward declaration to avoid circular imports

class Article(Base):
    """Database model for news articles."""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(255), nullable=True)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)

    def to_schema(self):
        """Converts the SQLAlchemy model instance into a Pydantic schema."""
        from schemas.articles import ArticleSchema  # Import inside the function to avoid circular import
        return ArticleSchema.from_orm(self)
