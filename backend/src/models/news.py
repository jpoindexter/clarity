from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String, Text
from backend.src.models import Base  # ✅ Ensure correct Base import


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String, nullable=False)  # ✅ Required
    url = Column(String, nullable=False)  # ✅ Required
    created_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    published_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )  # ✅ Ensure this is added!
