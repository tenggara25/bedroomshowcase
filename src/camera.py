import math
from src.math3d import normalize, cross, clamp, deg2rad
from src import config

class Camera:
    def __init__(self, pos=config.CAM_POS, yaw=config.CAM_YAW, pitch=config.CAM_PITCH):
        self.x, self.y, self.z = pos
        self.yaw = yaw
        self.pitch = pitch
        self.speed = config.CAM_SPEED
        self.sens = config.CAM_SENS

    def _front(self):
        yaw_r = deg2rad(self.yaw)
        pit_r = deg2rad(self.pitch)
        fx = math.cos(yaw_r) * math.cos(pit_r)
        fy = math.sin(pit_r)
        fz = math.sin(yaw_r) * math.cos(pit_r)
        return normalize(fx, fy, fz)

    def update_mouse(self, dx, dy):
        self.yaw += dx * self.sens
        self.pitch -= dy * self.sens
        self.pitch = clamp(self.pitch, -89.0, 89.0)

    def move(self, forward, right, dt):
        fx, fy, fz = self._front()
        rx, ry, rz = cross(fx, fy, fz, 0.0, 1.0, 0.0)
        rx, ry, rz = normalize(rx, ry, rz)

        v = self.speed * dt
        self.x += fx * forward * v + rx * right * v
        self.z += fz * forward * v + rz * right * v

    def look_at_args(self):
        fx, fy, fz = self._front()
        return (self.x, self.y, self.z,
                self.x + fx, self.y + fy, self.z + fz,
                0.0, 1.0, 0.0)
