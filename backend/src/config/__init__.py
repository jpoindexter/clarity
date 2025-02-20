"""
Configuration Initialization.

Ensures that settings are properly loaded when importing from `backend.src.config`.
"""

# ✅ Ensure absolute import from config.py
from backend.src.config.config import settings

# ✅ Confirm initialization
print("✅ backend.src.config initialized successfully!")

# ✅ Explicitly define what gets imported when using `from backend.src.config import *`
__all__ = ["settings"]
