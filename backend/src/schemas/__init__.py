# ✅ Use Lazy Import to Avoid Circular Dependencies
import backend.src.schemas.article as article_schema
import backend.src.schemas.news as news_schema

__all__ = ["article_schema", "news_schema"]