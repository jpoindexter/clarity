from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class NewsBase(BaseModel):
    """Base schema for all fetched news articles."""

    title: str
    content: str
    source: str
    url: str
    published_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )  # ✅ Fix: Optional


class News(NewsBase):
    """Schema for a stored news entry."""

    id: int


class NewsCreate(NewsBase):
    """Schema for creating new news articles."""

    pass


class NewsUpdate(BaseModel):
    """Schema for updating a news record."""

    title: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    published_at: Optional[datetime] = None
