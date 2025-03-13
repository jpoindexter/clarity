# ✅ backend/config/__init__.py
from backend.config.config import DATABASE_URL, BACKEND_HOST, BACKEND_PORT

# ✅ Prevent circular imports
__all__ = ["DATABASE_URL", "BACKEND_HOST", "BACKEND_PORT"]
