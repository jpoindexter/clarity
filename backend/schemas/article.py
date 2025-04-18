from datetime import datetime, timezone
from typing import Optional, Literal, List
from pydantic import BaseModel, Field, ConfigDict


class ArticleBase(BaseModel):
    """✅ Base schema for an article, used for creation & updates."""

    title: str
    summary: Optional[str] = None
    content: str
    source: str
    url: str
    published_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    credibility_score: Optional[float] = Field(
        None, description="AI-assigned credibility score (0-1)"
    )
    ai_summary: Optional[str] = Field(
        None, description="AI-generated summary for deeper insights"
    )


class Article(ArticleBase):
    """✅ Full schema for an article, including the unique ID."""

    id: int


class ArticleCreate(ArticleBase):
    """✅ Schema for creating new articles."""

    pass


class ArticleUpdate(BaseModel):
    """✅ Schema for updating articles."""

    title: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    published_at: Optional[datetime] = None
    credibility_score: Optional[float] = None
    ai_summary: Optional[str] = None


class ArticleIngestRequest(BaseModel):
    """🆕 Request schema for /articles/ingest endpoint"""
    source: Literal["url", "rss"]
    input: str


class SummarizedArticle(BaseModel):
    """🆕 Response schema for summarized articles"""
    title: str
    url: str
    summary: str
    source: str
    published: Optional[str] = None 
    tags: Optional[List[str]] = Field(
        default=None,
        description="List of tags or classifications assigned by AI"
    )


class SummarizedArticleCreate(BaseModel):
    """🆕 Input schema for creating summarized articles in DB"""
    title: str
    url: str
    summary: str
    tags: List[str]
    tone: str
    source: str
    raw_text: str


class ArticleOut(BaseModel):
    """✅ Output schema for serialized summarized article data."""
    id: int
    title: str
    url: str
    summary: str
    tags: Optional[List[str]] = None
    tone: Optional[str] = None
    source: str
    published_at: datetime

    model_config = ConfigDict(from_attributes=True) 