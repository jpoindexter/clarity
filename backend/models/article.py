from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String, Text, Float
from sqlalchemy.dialects.postgresql import JSONB
from backend.models import Base  # ✅ Ensure correct Base import
 

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    summary = Column(Text, nullable=False)  # ✅ Required
    content = Column(Text, nullable=False)
    source = Column(String, nullable=False)  # ✅ Required
    url = Column(String, nullable=False)
    published_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )  # ✅ Ensure default is set!


class SummarizedArticle(Base):
    __tablename__ = "summarized_articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    summary = Column(Text, nullable=False)
    tags = Column(JSONB)  # Store as comma-separated or JSON string
    tone = Column(String, nullable=True)
    manipulation_risk = Column(Float, nullable=True)
    source = Column(String, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    raw_text = Column(Text, nullable=True) 