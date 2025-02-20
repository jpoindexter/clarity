# backend/src/utils/timer.py

import time


class Timer:
    """A simple timer for measuring execution time."""

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
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
