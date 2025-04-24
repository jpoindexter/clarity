from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class SummarizedArticle(Base):
    __tablename__ = "summarized_articles"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    summary = Column(String, nullable=False)
    tone = Column(String, nullable=False)
    tags = Column(String, nullable=False)  # Store as a comma-separated string
    source = Column(String, nullable=False)
    raw_text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    manipulation_risk = Column(Float, nullable=False)