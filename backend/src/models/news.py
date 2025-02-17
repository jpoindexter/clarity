from sqlalchemy import Column, Integer, String, DateTime, Text
from backend.src.database.db_connection import Base  # ✅ Correct import path
from datetime import datetime, timezone

class News(Base):
    """✅ Database model for storing news articles."""
    
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)  # ✅ Limit to 255 chars for indexing efficiency
    content = Column(Text, nullable=False)  # ✅ Use `Text` for larger news articles
    source = Column(String(255), nullable=False)  # ✅ Must be NOT NULL
    url = Column(String(2083), nullable=False, unique=True)  # ✅ Standard max URL length, enforce uniqueness
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)  # ✅ Fixed deprecation warning

    def __repr__(self):
        """✅ Readable string representation of a News object."""
        return f"<News(id={self.id}, title={self.title}, source={self.source}, created_at={self.created_at})>"
