# ✅ Import all models so Alembic can detect them
from backend.src.database.db_connection import Base
from backend.src.models.article import Article
from backend.src.models.news import News

__all__ = ["News", "Article", "Base"]
