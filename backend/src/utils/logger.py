"""
Logging Utility Module
Provides a standardized logger for Clarity.
"""

import logging
import os

# Ensure logs directory exists
LOGS_DIR = os.path.join(os.path.dirname(__file__), "../../logs")
os.makedirs(LOGS_DIR, exist_ok=True)


def setup_logger(
    name: str, log_file: str = "backend.log", level=logging.INFO
) -> logging.Logger:
    """
    Set up a logger for a specific module or service.

    Args:
        name (str): Name of the logger.
        log_file (str): Log file name (default: backend.log).
        level: Logging level (default: INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
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
