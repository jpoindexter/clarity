from database.db_helper import get_db_connection

def test_db_connection():
    db = get_db_connection()
    assert db is not None