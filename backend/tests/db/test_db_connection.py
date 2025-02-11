from backend.database.db_connection_connection import fetch_articles, get_db_connection  # ✅ Fixed import

def test_db_connection():
    """Ensure that the database connection is established properly."""
    db = get_db_connection()
    assert db is not None, "Database connection failed"
