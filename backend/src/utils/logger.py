# backend/src/utils/logger.py

import logging
import os

LOGS_DIR = os.path.join(os.path.dirname(__file__), "../../logs")
os.makedirs(LOGS_DIR, exist_ok=True)  # Ensure logs directory exists


def setup_logger(name, log_file="backend.log", level=logging.INFO):
    """Set up a logger for a specific module or service."""
    log_path = os.path.join(LOGS_DIR, log_file)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler(log_path)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False

    return logger


# Example usage:
# logger = setup_logger(__name__)
# logger.info("Logger initialized.")
