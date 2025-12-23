import time

class Time:
    def __init__(self):
        self._last = time.perf_counter()
        self.dt = 0.0

    def tick(self):
        now = time.perf_counter()
        self.dt = max(0.0, now - self._last)
        self._last = now
        return self.dt
