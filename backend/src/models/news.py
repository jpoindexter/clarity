from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String, Text

from backend.src.database.db_connection import Base  # ✅ Fixed import


class News(Base):
    """✅ Database model for storing news articles."""

    __tablename__ = "news"
    __table_args__ = {"extend_existing": True}  # ✅ Fixes duplicate table error

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(255), nullable=False)
    url = Column(String(2083), nullable=False, unique=True)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )  # ✅ Line split for PEP8 compliance

    def __repr__(self):
        return (
            f"<News(id={self.id}, title={self.title}, "
            f"source={self.source}, "
            f"created_at={self.created_at})>"
        )  # ✅ Line split for PEP8 compliance
