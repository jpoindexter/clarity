# ✅ Import all models so Alembic can detect them
from src.models.news import News
from src.models.article import Article
from src.database.db_connection import Base  

__all__ = ["News", "Article", "Base"]
