<<<<<<< HEAD
# ✅ backend/src/config/__init__.py
=======
# ✅ backend/config/__init__.py
>>>>>>> e7de5aae97128e25160c3ae83bd7e7b38dfd0917
from backend.config.config import DATABASE_URL, BACKEND_HOST, BACKEND_PORT

# ✅ Prevent circular imports
__all__ = ["DATABASE_URL", "BACKEND_HOST", "BACKEND_PORT"]
