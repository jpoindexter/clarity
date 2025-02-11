import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ✅ Use a test database for pytest, fallback to real DB otherwise
DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_db")
if "PYTEST_RUNNING" in os.environ:
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test_db"  # ✅ Use test DB

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
