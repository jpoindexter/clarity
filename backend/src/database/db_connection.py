"""
Database connection setup and helper functions.
"""

import os
import pytest  # ✅ Ensure pytest is imported for fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

# ✅ Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://jpoindexter:dontforgetme@localhost:5432/clarity")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_clarity")

# ✅ Ensure database URLs are set
if not DATABASE_URL or not TEST_DATABASE_URL:
    raise ValueError("❌ DATABASE_URL or TEST_DATABASE_URL is not set. Check your environment variables.")

# ✅ Create database engines
engine = create_engine(DATABASE_URL)
test_engine = create_engine(TEST_DATABASE_URL)

# ✅ Standard Session for Main Application
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Scoped Session for Testing
TestingSessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=test_engine))

# ✅ Define Base model
Base = declarative_base()

# ✅ Import models to ensure they are registered before migrations
from backend.src.models import news, article  # Ensure all models are loaded

# ✅ Dependency for DB session
def get_db():
    """Create a new database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Dependency for Test DB session (for pytest)
def get_test_db():
    """Create a new test database session for testing."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Pytest fixture to ensure test DB session works
@pytest.fixture
def test_db():
    """Provides a test database session."""
    db = next(get_test_db())  # ✅ Use the test DB function
    yield db
    db.close()