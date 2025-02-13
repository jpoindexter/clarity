import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://jpoindexter:dontforgetme@localhost:5432/clarity")

# ✅ Create database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Define Base model
Base = declarative_base()

# ✅ Dependency for DB session
def get_db():
    """Create a new database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# ✅ Import database connection and all models