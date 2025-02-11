import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.db_connection import get_db  # ✅ Ensures correct dependency injection
from src.models.article import Base  # ✅ Correct import from refactored structure

# ✅ Use a temporary PostgreSQL test database
TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_db"
)

@pytest.fixture(scope="session")
def test_engine():
    """Creates a test database engine."""
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="session")
def test_db(test_engine):
    """Creates a temporary test session and provides a clean database."""
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=test_engine
    )

    def override_get_db():
        """Dependency override to use the test database."""
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    yield override_get_db  # ✅ Yield test DB session
