import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.src.models import Base  # ✅ Ensure models are imported

# ✅ Load database URL from environment or fallback to SQLite (for local testing)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///backend/src/database/db.sqlite3")

# ✅ Configure SQLAlchemy engine with proper connection settings
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    echo=True  # ✅ Enables SQL query logging for debugging
)

# ✅ Create session factory & scoped session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)

# ✅ Ensure database schema is created
Base.metadata.create_all(bind=engine)

# ✅ Dependency for getting database session
def get_db():
    """Yield a database session and ensure it's closed after use."""
    db = Session()
    try:
        yield db
    finally:
        db.close()

# ✅ Dependency for test database session
def get_test_db():
    """Provide a separate database session for tests."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
