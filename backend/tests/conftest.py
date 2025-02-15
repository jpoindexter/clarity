import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://jpoindexter:dontforgetme@localhost:5432/clarity")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_clarity")

# ✅ Ensure database URL is set
if not TEST_DATABASE_URL:
    raise ValueError("❌ TEST_DATABASE_URL is not set. Check your environment variables.")

# ✅ Create test database engine
test_engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# ✅ Define Base model
Base = declarative_base()

# ✅ Import from db_connection.py
from backend.src.database.db_connection import get_test_db  # ✅ Ensure function exists

# ✅ Pytest fixture for test DB session
@pytest.fixture(scope="session")
def test_db():
    """Provides a test database session."""
    db = next(get_test_db())  # ✅ Use the correct test DB function
    yield db
    db.close()