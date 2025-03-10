import os
import logging
from contextlib import contextmanager
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
# ✅ Import models **first** to comply with Flake8 E402
from backend.src.models import Base

# ✅ Load DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set. Please define it in the environment.")

# ✅ Configure PostgreSQL engine with efficient pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # ✅ Maintain up to 10 active connections
    max_overflow=20,       # ✅ Allow 20 additional temporary connections
    pool_timeout=30,       # ✅ Max time to wait for connection
    pool_recycle=1800,     # ✅ Prevents stale connections
    echo=False,            # ✅ Disables excessive SQL logging
)

# ✅ Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)

# ✅ Ensure tables exist before first request
try:
    with engine.connect() as connection:
        inspector = inspect(connection)
        tables_to_check = ["articles"]  # ✅ List your tables here
        for table in tables_to_check:
            if not inspector.has_table(table):  # ✅ Fix for has_table()
                Base.metadata.create_all(bind=engine)
except Exception as e:
    logging.error(f"❌ Database Initialization Failed: {e}")


# ✅ Dependency Injection for FastAPI
def get_db():
    """✅ Provide database session with proper cleanup."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Context manager for manual session handling (if needed outside FastAPI)
@contextmanager
def get_session():
    """✅ Provides a session and ensures it closes properly."""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
