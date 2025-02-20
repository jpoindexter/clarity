"""
Database connection setup and helper functions.
"""

import importlib
import logging
import os

import pytest  # ✅ Ensure pytest is imported for fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

# ✅ Enable Query Logging (Useful for Debugging & Optimization)
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# ✅ Load environment variables (DO NOT HARDCODE CREDENTIALS)
DATABASE_URL = os.getenv("DATABASE_URL")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

# ✅ Ensure database URLs are set
if not DATABASE_URL or not TEST_DATABASE_URL:
    raise ValueError(
        "❌ DATABASE_URL or TEST_DATABASE_URL is not set.\n"
        "   ➜ Check your environment variables."
    )

# ✅ Create database engines with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,  # ✅ Allow up to 10 connections
    max_overflow=20,  # ✅ Allow 20 additional connections in bursts
    pool_timeout=30,  # ✅ Wait 30s before giving up
    pool_recycle=1800,  # ✅ Recycle connections every 30 minutes
)

test_engine = create_engine(TEST_DATABASE_URL, echo=True)  # ✅ Enable logging for tests

# ✅ Standard Session for Main Application
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# ✅ Scoped Session for Testing
TestingSessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=test_engine,
    )
)

# ✅ Define Base model
Base = declarative_base()

# ✅ Dynamically import models to avoid circular imports
MODELS = ["news", "article"]  # ✅ Only valid models, no "backend" nonsense

for model in MODELS:
    module_path = f"backend.src.models.{model}"
    try:
        print(f"🔍 Importing model: {module_path}")
        importlib.import_module(module_path)
    except ModuleNotFoundError as e:
        print(f"❌ Model Import Failed: {module_path}\n   ➜ Error: {e}")

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
    TestingSessionLocal.remove()  # ✅ Dispose of scoped session after tests