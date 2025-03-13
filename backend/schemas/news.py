from datetime import datetime, timezone
from typing import Optional
<<<<<<< HEAD

=======
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
from pydantic import BaseModel, Field


class NewsBase(BaseModel):
    """Base schema for all fetched news articles."""
<<<<<<< HEAD

    title: str
=======
    title: str
    summary: Optional[str] = None  # Added summary based on schema design
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
    content: str
    source: str
    url: str
    published_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
<<<<<<< HEAD
    )  # ✅ Fix: Optional


class News(NewsBase):
    """Schema for a stored news entry."""

=======
    )


class NewsSchema(NewsBase):  # Ensuring the correct class exists
    """Schema for a stored news entry."""
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
    id: int


class NewsCreate(NewsBase):
    """Schema for creating new news articles."""
<<<<<<< HEAD

=======
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
    pass


class NewsUpdate(BaseModel):
    """Schema for updating a news record."""
<<<<<<< HEAD

    title: Optional[str] = None
=======
    title: Optional[str] = None
    summary: Optional[str] = None
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
    content: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    published_at: Optional[datetime] = None
