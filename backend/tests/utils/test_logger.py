# backend/tests/utils/test_logger.py
from utils.logger import setup_logger

def test_logger():
    logger = setup_logger("test")
    assert logger is not None
