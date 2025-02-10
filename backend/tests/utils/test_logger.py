from utils.logger import setup_logger

def test_setup_logger():
    logger = setup_logger(__name__)
    assert logger is not None