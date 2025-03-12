from .news import news_crud  # ✅ Industry standard naming

__all__ = ["news_crud"]  # ✅ Explicitly exposing news_crud

from .news import news_crud  # Ensure correct import
