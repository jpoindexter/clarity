import pytest
from backend.src.database.db_connection import get_db, SessionLocal


def test_get_db():
    """✅ Ensure DB session opens and closes properly."""
    db = next(get_db())
    try:
        assert db is not None, "Database session should not be None"
    finally:
        db.close()  # ✅ Ensure session closes properly


def test_session_commit():
    """✅ Ensure session commit does not fail."""
    db = SessionLocal()
    try:
        db.commit()
        assert True  # ✅ Explicit success condition
    except Exception as e:
        pytest.fail(f"Commit failed unexpectedly: {e}")
    finally:
        db.close()  # ✅ Ensure session closes properly
