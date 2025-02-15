import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# ✅ Ensure the `src` folder is added to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from backend.src.database.db_connection import get_db
from backend.src.models.article import Base  # ✅ Ensure Base is imported for table creation

# ✅ Load test database URL
TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_db"
)


@pytest.fixture(scope="session")
def test_engine():
    """Creates a test database engine."""
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(bind=engine)  # ✅ Create tables
    yield engine
    Base.metadata.drop_all(bind=engine)  # ✅ Cleanup


@pytest.fixture(scope="session")
def test_db(test_engine):
    """Creates a test database session."""
    TestingSessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    )

    def override_get_db():
        """Dependency override for using the test database."""
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    yield override_get_db  # ✅ Yield the test DB session
    TestingSessionLocal.remove()  # ✅ Cleanup session


@pytest.fixture(scope="module")
def db_session(test_db):
    """Provides a clean test database session for each test module."""
    yield from test_db()


@pytest.fixture(autouse=True)
def reset_database(test_engine):
    """Ensure the database is reset between test runs."""
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
