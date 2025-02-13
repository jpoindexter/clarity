from pydantic import BaseModel, ConfigDict, field_serializer
from datetime import datetime
from typing import Optional

class NewsBase(BaseModel):
    title: str
    content: str
    source: str
    url: str

class NewsCreate(NewsBase):
    pass

class NewsUpdate(BaseModel):  # ✅ Add this to allow updates
    title: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None

class News(NewsBase):
    id: int
    created_at: datetime  # ✅ Store as datetime, Pydantic will serialize it

    @field_serializer("created_at")
    def serialize_created_at(self, value: datetime) -> str:
        """ Convert datetime to string automatically in responses. """
        return value.isoformat()

    model_config = ConfigDict(from_attributes=True)  # ✅ Ensures correct ORM parsing
