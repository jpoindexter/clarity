# backend/tests/utils/test_helpers.py
from backend.src.utils.helpers import clean_text

def test_clean_text():
    assert clean_text(" Hello  World ") == "Hello World"
