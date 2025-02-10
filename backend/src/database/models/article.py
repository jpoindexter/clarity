from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Article(Base):
    """Database model for news articles."""
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(255), nullable=True)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)

