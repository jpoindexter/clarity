from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String, Text
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
