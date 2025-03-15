from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class NewsBase(BaseModel):
    """Base schema for all fetched news articles."""

    title: str
    summary: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    published_at: Optional[datetime] = None


class NewsCreate(NewsBase):
    """Schema for creating a new news entry."""
    pass


class News(NewsBase):
    """Schema for a stored news entry."""
    id: int

    model_config = ConfigDict(from_attributes=True)


class NewsUpdate(NewsBase):
    """Schema for updating a news record."""
    title: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    published_at: Optional[datetime] = None
