from pydantic import BaseModel

class NewsCreate(BaseModel):
    title: str
    content: str
    source: str
    url: str

class NewsUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    source: str | None = None
    url: str | None = None

class News(NewsCreate):
    id: int

    class Config:
        from_attributes = True
