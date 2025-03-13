<<<<<<< HEAD
# ✅ backend/src/models/__init__.py
=======
# ✅ backend/models/__init__.py
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917

from sqlalchemy.orm import declarative_base

# ✅ Define Base FIRST to avoid circular imports
Base = declarative_base()

# ✅ Import models AFTER defining Base to prevent circular imports
import backend.models.article  # noqa: E402, F401
import backend.models.news  # noqa: E402, F401

# ✅ Ensure Base is available globally
__all__ = ["Base"]
