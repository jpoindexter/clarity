# ✅ backend/src/models/__init__.py
from sqlalchemy.orm import declarative_base

# ✅ Define Base FIRST to avoid circular imports
Base = declarative_base()

# ✅ Import models AFTER defining Base to prevent circular imports
import backend.src.models.article
import backend.src.models.news

# ✅ Ensure Base is available globally
__all__ = ["Base"]