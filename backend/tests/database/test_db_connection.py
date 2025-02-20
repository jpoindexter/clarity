import pytest
from backend.src.database.db_connection import get_db, get_test_db, SessionLocal


def test_get_db():
    """✅ Ensure DB session opens and closes properly"""
    db = next(get_db())
    assert db is not None
    db.close()


def test_get_test_db():
    """✅ Ensure Test DB session opens and closes properly"""
    test_db = next(get_test_db())
    assert test_db is not None
    test_db.close()


def test_session_commit():
    """✅ Ensure session commit does not fail"""
    db = SessionLocal()
    try:
        db.commit()
    except Exception:
        assert False, "Commit failed unexpectedly"
    finally:
        db.close()