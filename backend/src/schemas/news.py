from pydantic import BaseModel, ConfigDict, field_serializer, Field
from datetime import datetime
from typing import Optional

class NewsBase(BaseModel):
    title: str
    content: str
    source: str
    url: str

class NewsCreate(NewsBase):
    pass

class NewsUpdate(BaseModel):
    """✅ Schema for updating news entries"""
    title: Optional[str] = Field(None, min_length=1)  # ✅ Title cannot be None
    content: Optional[str]
    source: Optional[str]
    url: Optional[str]

    class Config:
        from_attributes = True

class News(NewsBase):
    id: int
    created_at: datetime  # ✅ Store as datetime, Pydantic will serialize it

    @field_serializer("created_at")
    def serialize_created_at(self, value: datetime) -> str:
        """ Convert datetime to string automatically in responses. """
        return value.isoformat()

    model_config = ConfigDict(from_attributes=True)  # ✅ Ensures correct ORM parsing
