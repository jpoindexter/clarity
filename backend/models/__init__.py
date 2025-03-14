# ✅ backend/models/__init__.py

from sqlalchemy.orm import declarative_base

# ✅ Define Base FIRST to avoid circular imports
Base = declarative_base()

# ✅ Import models AFTER defining Base to prevent circular imports
from backend.models import article  # noqa: E402, F401
from backend.models import news  # noqa: E402, F401

# ✅ Ensure Base is available globally
__all__ = ["Base", "article", "news"]
