"""
Article Model Definition.

Defines the SQLAlchemy model for storing article data in the database.
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, func
from ..database.db_connection import Base  # ✅ Correct import path

class Article(Base):
    """Database model for storing articles."""

    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)  # ✅ Limit title length
    summary = Column(Text, nullable=True)
    content = Column(Text, nullable=False)  # ✅ Ensures articles always have content
    source = Column(String(255), nullable=False)  
    url = Column(
        String(2083), nullable=False, unique=True
    )  # ✅ Fix line-too-long issue by splitting URL column
    published_at = Column(
        DateTime, server_default=func.now(), nullable=False
    )  # ✅ Fix `func.now()` and line length
    category = Column(String(100), nullable=True)  

    def __repr__(self):
        """Readable string representation of an Article object."""
        return (
            f"<Article(id={self.id}, title={self.title}, source={self.source}, "
            f"published_at={self.published_at})>"
        )  # ✅ Fix line-too-long issue by splitting it into multiple lines
