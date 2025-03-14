from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class NewsBase(BaseModel):
    """Base schema for all fetched news articles."""

    title: str
    summary: Optional[str] = None  # Added summary based on schema design


class News(NewsBase):
    """Schema for a stored news entry."""
    pass


class NewsUpdate(BaseModel):
    """Schema for updating a news record."""
    title: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    published_at: Optional[datetime] = None
