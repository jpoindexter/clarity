# backend/tests/db/test_db_connection.py
from database.db_helper import get_db_connection

def test_db_connection():
    conn = get_db_connection()
    assert conn is not None
    conn.close()
