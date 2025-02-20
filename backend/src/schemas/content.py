from pydantic import BaseModel, ConfigDict


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

    class YourModel(BaseModel):
        model_config = ConfigDict(arbitrary_types_allowed=True)
