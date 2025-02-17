from sqlalchemy import Column, Integer, String, DateTime, Text
from backend.src.database.db_connection import Base
from datetime import datetime, timezone

class News(Base):
    """✅ Database model for storing news articles."""
    
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(255), nullable=False)
    url = Column(String(2083), nullable=False, unique=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        return f"<News(id={self.id}, title={self.title}, source={self.source}, created_at={self.created_at})>"