from pydantic import BaseModel

class ArticleCreate(BaseModel):
    title: str
    content: str
    source: str  # ✅ Required
    url: str  # ✅ Now stored as `str` instead of `HttpUrl`

class Article(BaseModel):
    id: int
    title: str
    content: str
    source: str
    url: str  # ✅ Updated to `str`

    class Config:
        from_attributes = True
