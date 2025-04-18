from sqlalchemy import Column, Integer, String, DateTime
from backend.database.base import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(String, index=True)
    content = Column(String)
    source = Column(String)
    url = Column(String)
    published_at = Column(DateTime)

from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime

class SummarizedArticle(Base):
    __tablename__ = "summarized_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String, unique=True, index=True)
    summary = Column(Text)
    tags = Column(ARRAY(String))  # For SQLite, consider using JSON
    tone = Column(String)
    source = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    raw_text = Column(Text)