from pydantic import BaseModel, Field
from datetime import datetime

class NewsCreate(BaseModel):
    title: str
    content: str
    source: str = Field(..., description="Source is required")  # ✅ REQUIRED
    url: str = Field(..., description="URL is required")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ArticleCreate(BaseModel):
    title: str
    summary: str = Field(..., description="Summary is required")  # ✅ REQUIRED
    content: str
    source: str = Field(..., description="Source is required")
    url: str
    published_at: datetime = Field(default_factory=datetime.utcnow)