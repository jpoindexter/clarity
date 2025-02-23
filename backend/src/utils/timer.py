"""
Timer Utility Module
Provides utilities for measuring execution time.
"""

import time


class Timer:
    """
    A simple timer for measuring execution time.
    """

    def __init__(self):
        self.start_time = None

    def start(self):
        """
        Starts the timer.
        """
        self.start_time = time.time()

    def stop(self) -> float:
        """
        Stops the timer and returns elapsed time.

        Returns:
            float: Elapsed time in seconds.

        Raises:
            ValueError: If the timer was never started.
        """
        if self.start_time is None:
            raise ValueError("Timer was never started.")
        elapsed_time = time.time() - self.start_time
        self.start_time = None
        return elapsed_time


# Example usage:
# timer = Timer()
# timer.start()
# ... (code execution) ...
# print(f"Execution Time: {timer.stop()} seconds")
