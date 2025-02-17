from sqlalchemy import Column, Integer, String, DateTime, Text
from backend.src.database.db_connection import Base
from datetime import datetime, timezone

class Article(Base):
    """✅ Database model for storing articles."""
    
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    summary = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(255), nullable=False)
    url = Column(String(2083), nullable=False, unique=True)
    published_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        return f"<Article(id={self.id}, title={self.title}, source={self.source}, published_at={self.published_at})>"