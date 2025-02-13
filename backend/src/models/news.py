from sqlalchemy import Column, Integer, String, DateTime
from src.database.db_connection import Base
import datetime

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    source = Column(String, nullable=False)  # ✅ Must be NOT NULL
    url = Column(String, nullable=False)  # ✅ Must be NOT NULL
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
