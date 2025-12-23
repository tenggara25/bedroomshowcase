import math

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def normalize(x, y, z):
    mag = math.sqrt(x*x + y*y + z*z)
    if mag == 0:
        return 0.0, 0.0, 0.0
    return x/mag, y/mag, z/mag

def cross(ax, ay, az, bx, by, bz):
    return (ay*bz - az*by, az*bx - ax*bz, ax*by - ay*bx)

def deg2rad(d):
    return d * math.pi / 180.0
