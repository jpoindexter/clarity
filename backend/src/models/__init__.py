from sqlalchemy.orm import declarative_base

Base = declarative_base()  # ✅ No circular import

# ✅ Import models AFTER defining Base
import backend.src.models.article
import backend.src.models.news
import backend.src.database.db_connection as db_conn