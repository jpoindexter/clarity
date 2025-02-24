# ✅ backend/src/models/__init__.py

from sqlalchemy.orm import declarative_base

# ✅ Define Base FIRST to avoid circular imports
Base = declarative_base()

# ✅ Import models AFTER defining Base to prevent circular imports
import backend.src.models.article  # noqa: E402, F401
import backend.src.models.news  # noqa: E402, F401

# ✅ Ensure Base is available globally
__all__ = ["Base"]

# ✅ Add a newline at the end of file (Fixes W292)
