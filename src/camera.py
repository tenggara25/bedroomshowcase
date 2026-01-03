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
        
        # Collision bounds (room boundaries)
        self.min_x = -3.7
        self.max_x = 3.7
        self.min_z = -3.7
        self.max_z = 3.7
        self.collision_radius = 0.3

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

    def _check_collision(self, new_x, new_z):
        """Check if new position collides with walls or objects"""
        # Wall collision
        if new_x < self.min_x + self.collision_radius:
            new_x = self.min_x + self.collision_radius
        if new_x > self.max_x - self.collision_radius:
            new_x = self.max_x - self.collision_radius
        if new_z < self.min_z + self.collision_radius:
            new_z = self.min_z + self.collision_radius
        if new_z > self.max_z - self.collision_radius:
            new_z = self.max_z - self.collision_radius
        
        # Simple object collision (AABB)
        obstacles = [
            # Bed area
            {"min": (-3.8, -3.2), "max": (-1.3, -1.8)},
            # Desk area
            {"min": (2.4, -2.5), "max": (3.9, -1.5)},
            # Wardrobe area
            {"min": (-3.9, 0.8), "max": (-3.2, 2.2)},
            # Bookshelf area
            {"min": (0.4, -3.9), "max": (1.6, -3.5)},
            # Nightstand area
            {"min": (-1.5, -2.8), "max": (-0.9, -2.2)},
        ]
        
        for obs in obstacles:
            min_x, min_z = obs["min"]
            max_x, max_z = obs["max"]
            
            # Check if player would be inside obstacle
            if (min_x - self.collision_radius < new_x < max_x + self.collision_radius and
                min_z - self.collision_radius < new_z < max_z + self.collision_radius):
                # Push player out
                # Find closest edge
                dx_left = abs(new_x - (min_x - self.collision_radius))
                dx_right = abs(new_x - (max_x + self.collision_radius))
                dz_back = abs(new_z - (min_z - self.collision_radius))
                dz_front = abs(new_z - (max_z + self.collision_radius))
                
                min_dist = min(dx_left, dx_right, dz_back, dz_front)
                
                if min_dist == dx_left:
                    new_x = min_x - self.collision_radius
                elif min_dist == dx_right:
                    new_x = max_x + self.collision_radius
                elif min_dist == dz_back:
                    new_z = min_z - self.collision_radius
                else:
                    new_z = max_z + self.collision_radius
        
        return new_x, new_z

    def move(self, forward, right, dt):
        fx, fy, fz = self._front()
        rx, ry, rz = cross(fx, fy, fz, 0.0, 1.0, 0.0)
        rx, ry, rz = normalize(rx, ry, rz)

        v = self.speed * dt
        new_x = self.x + fx * forward * v + rx * right * v
        new_z = self.z + fz * forward * v + rz * right * v
        
        # Apply collision detection
        self.x, self.z = self._check_collision(new_x, new_z)

    def look_at_args(self):
        fx, fy, fz = self._front()
        return (self.x, self.y, self.z,
                self.x + fx, self.y + fy, self.z + fz,
                0.0, 1.0, 0.0)
