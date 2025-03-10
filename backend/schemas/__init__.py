# ✅ Use Lazy Import to Avoid Circular Dependencies
import backend.schemas.article as article_schema
import backend.schemas.news as news_schema

__all__ = ["article_schema", "news_schema"]
