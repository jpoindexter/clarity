import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))  

pytest_plugins = [
    "tests.fixtures.database",
    "tests.fixtures.client",
]  # ✅ Ensures Pytest finds fixtures correctly

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .database.db_connection import get_db  # ✅ Removed `src.`
from .models.article import Base  # ✅ Removed `src.`

# ✅ Load test database URL from environment, with a fallback
TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_db"
)

@pytest.fixture(scope="session")
def test_engine():
    """Creates a test database engine."""
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(bind=engine)  # ✅ Ensure tables exist
    yield engine
    Base.metadata.drop_all(bind=engine)  # ✅ Clean up after tests

@pytest.fixture(scope="session")
def test_db(test_engine):
    """Creates a test database session and ensures clean state."""
    TestingSessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    )

    def override_get_db():
        """Dependency override for using test database."""
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    yield override_get_db  # ✅ Yield the test DB session
    TestingSessionLocal.remove()  # ✅ Cleanup session

@pytest.fixture(autouse=True)
def reset_database(test_engine):
    """Ensure the database is reset between test runs."""
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
