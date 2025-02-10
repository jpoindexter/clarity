from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from backend.src.database.db_connection import Base  # Ensure this import is correct

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)
    author = Column(String(100), nullable=True)  # New column added
    created_at = Column(TIMESTAMP, server_default=func.now())

