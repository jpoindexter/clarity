import os
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from alembic.config import Config
from alembic import command

# ✅ Load test database environment variable
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "sqlite:///test_clarity.db")

# ✅ Ensure TEST_DATABASE_URL is set
if not TEST_DATABASE_URL:
    raise ValueError("❌ TEST_DATABASE_URL is not set. Check your environment variables.")

# ✅ Create test database engine
if TEST_DATABASE_URL.startswith("sqlite"):
    test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    test_engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=test_engine))

from backend.src.database.db_connection import Base, get_test_db

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """✅ Ensure test database is created & migrations are applied before running tests."""
    
    # ✅ Ensure database file exists
    if not os.path.exists("test_clarity.db"):
        open("test_clarity.db", "w").close()  # Create empty DB file

    with test_engine.connect() as conn:
        conn.execute(text("SET session_replication_role = 'replica';"))  # ✅ PostgreSQL alternative 
        conn.commit()

    # ✅ Apply Alembic migrations to create tables
    alembic_cfg = Config("backend/alembic.ini")  # ✅ Fix path
    alembic_cfg.set_main_option("sqlalchemy.url", TEST_DATABASE_URL)
    command.upgrade(alembic_cfg, "head")  # ✅ Apply all migrations

    yield  # ✅ Run tests

    # ✅ Drop schema after tests
    with test_engine.connect() as conn:
        conn.execute(text("PRAGMA foreign_keys=ON;"))  # Re-enable foreign key checks
        conn.commit()

@pytest.fixture(scope="function")
def test_db():
    """✅ Provides a clean database session for each test."""
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.rollback()  # ✅ Rollback changes after each test
        session.close()