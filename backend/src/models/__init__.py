# ✅ Import all models so Alembic can detect them
from models.news import News
from models.article import Article
from database.db_connection import Base  

__all__ = ["News", "Article", "Base"]
