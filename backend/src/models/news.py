from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String, nullable=False)  # ✅ Required
    url = Column(String, nullable=False)  # ✅ Required
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    published_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))  # ✅ Ensure this is added!


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    summary = Column(Text, nullable=False)  # ✅ Required
    content = Column(Text, nullable=False)
    source = Column(String, nullable=False)  # ✅ Required
    url = Column(String, nullable=False)
    published_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))  # ✅ Ensure default is set!
