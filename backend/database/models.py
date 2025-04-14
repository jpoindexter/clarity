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