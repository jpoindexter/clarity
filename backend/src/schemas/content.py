from pydantic import BaseModel

class ContentSchema(BaseModel):  # ✅ Add this missing schema
    title: str
    content: str

class ArticleCreate(BaseModel):
    title: str
    content: str
    source: str  
    url: str  

class Article(BaseModel):
    id: int
    title: str
    content: str
    source: str
    url: str  

    class Config:
        from_attributes = True
