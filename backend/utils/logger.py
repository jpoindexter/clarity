"""
Logging Utility Module
Provides a standardized logger for Clarity.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure logs directory exists
LOGS_DIR = os.path.join(os.path.dirname(__file__), "../../logs")
os.makedirs(LOGS_DIR, exist_ok=True)


def setup_logger(
    name: str,
    log_file: str = "backend.log",
    level=logging.INFO,
    max_bytes=5_000_000,
    backup_count=5,
) -> logging.Logger:
    """
    Set up a rotating logger for a specific module or service.

    Args:
        name (str): Name of the logger.
        log_file (str): Log file name (default: backend.log).
        level: Logging level (default: INFO).
        max_bytes (int): Max file size before rotation (default: 5MB).
        backup_count (int): Number of backup log files to keep.

    Returns:
        logging.Logger: Configured logger instance.
    """
    log_path = os.path.join(LOGS_DIR, log_file)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # File handler (rotates logs when they exceed max_bytes)
    file_handler = RotatingFileHandler(
        log_path, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setFormatter(formatter)

    # Console handler (prints logs to terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)  # Added console logging
    logger.propagate = False

    return logger


# Example usage:
# logger = setup_logger(__name__)
# logger.info("Logger initialized.")
