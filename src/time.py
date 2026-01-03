import time

class Time:
    def __init__(self):
        self._last = time.perf_counter()
        self.dt = 0.0
        self.fps = 0.0
        self._fps_accum = 0.0
        self._fps_frames = 0
        self._fps_update_interval = 0.5  # Update FPS setiap 0.5 detik

    def tick(self):
        now = time.perf_counter()
        self.dt = max(0.0, now - self._last)
        self._last = now
        
        # Calculate FPS
        self._fps_accum += self.dt
        self._fps_frames += 1
        
        if self._fps_accum >= self._fps_update_interval:
            self.fps = self._fps_frames / self._fps_accum
            self._fps_accum = 0.0
            self._fps_frames = 0
        
        return self.dt
