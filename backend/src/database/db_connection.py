# ✅ backend/src/database/db_connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///backend/src/database/db.sqlite3")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    echo=True  # ✅ Enables SQL query logging for debugging
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)

def get_db():
    """✅ Yield database session, closing after request."""
    db = Session()
    try:
        yield db
    finally:
        db.close()

# 🚀 Move model imports **below function definitions** to prevent circular imports
from backend.src.models import Base  

# ✅ Ensure models are registered correctly (Moved outside function to avoid recursion)
Base.metadata.create_all(bind=engine)
