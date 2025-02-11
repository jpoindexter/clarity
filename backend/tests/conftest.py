import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.db import get_db  # ✅ Fixed import
from src.database.models.article import Base  # ✅ Fixed import
import os

# ✅ Use a temporary PostgreSQL test database
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_db")

@pytest.fixture(scope="session")
def test_db():
    """Creates a temporary test database and cleans up after tests."""
    engine = create_engine(TEST_DATABASE_URL)  # ✅ Use the test DB URL
    Base.metadata.create_all(bind=engine)  # ✅ Create tables

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db():
        """Dependency override to use the test database."""
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    yield override_get_db  # ✅ Yield test DB session
    Base.metadata.drop_all(bind=engine)  # ✅ Cleanup after tests
