from pydantic import BaseModel

class NewsCreate(BaseModel):
    title: str
    content: str

class NewsUpdate(BaseModel):
    title: str
    content: str

class News(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True

