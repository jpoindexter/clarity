import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from backend.src.models import Base  # ✅ Ensure models are imported correctly

# ✅ Load DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set. Please define it in the environment.")

# ✅ Configure PostgreSQL engine
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    echo=True,  # ✅ Enables SQL query logging for debugging
)

# ✅ Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(SessionLocal)


def get_db():
    """✅ Yield database session, closing after request."""
    db = Session()
    try:
        yield db
    finally:
        db.close()


# ✅ Ensure models are registered correctly
Base.metadata.create_all(bind=engine)
