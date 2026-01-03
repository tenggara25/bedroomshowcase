from OpenGL.GL import *
from OpenGL.GLU import *
import math

class Renderer:
    def __init__(self):
        self.auto_tour = True
        self.focus_target = None
        self.focus_name = None
        self._t = 0.0
        
        # Smooth camera transition
        self._cam_pos = [0.0, 1.8, 2.8]  # Current interpolated position
        self._cam_look = [0.0, 1.2, 0.0]  # Current interpolated look-at
        self._transition_speed = 2.5  # Kecepatan transisi

    def init_gl(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)
        glDisable(GL_CULL_FACE)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    def set_projection(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/max(1,h), 0.1, 100)
        glMatrixMode(GL_MODELVIEW)

    def begin_frame(self, lighting):
        if lighting.mode == "day":
            glClearColor(0.6, 0.75, 0.95, 1)
        else:
            glClearColor(0.05, 0.05, 0.08, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

    def set_focus(self, pos, name):
        self.focus_target = pos
        self.focus_name = name
        self.auto_tour = False

    def clear_focus(self):
        self.focus_target = None
        self.focus_name = None

    def _lerp(self, a, b, t):
        """Linear interpolation"""
        return a + (b - a) * min(1.0, t)

    def _lerp_vec(self, current, target, t):
        """Lerp untuk vector 3D"""
        return [
            self._lerp(current[0], target[0], t),
            self._lerp(current[1], target[1], t),
            self._lerp(current[2], target[2], t),
        ]

    def apply_camera(self, cam, dt):
        t = self._transition_speed * dt
        
        if self.focus_target:
            # Target: kamera tetap, lihat ke focus_target
            target_pos = [cam.x, cam.y, cam.z]
            target_look = list(self.focus_target)
            
            self._cam_pos = self._lerp_vec(self._cam_pos, target_pos, t)
            self._cam_look = self._lerp_vec(self._cam_look, target_look, t)
            
            gluLookAt(
                self._cam_pos[0], self._cam_pos[1], self._cam_pos[2],
                self._cam_look[0], self._cam_look[1], self._cam_look[2],
                0, 1, 0
            )
            return

        if self.auto_tour:
            self._t += dt
            r = 2.8
            target_x = math.cos(self._t * 0.4) * r
            target_z = math.sin(self._t * 0.4) * r
            target_y = 1.8
            
            target_pos = [target_x, target_y, target_z]
            target_look = [0.0, 1.2, 0.0]
            
            # Smooth transition
            self._cam_pos = self._lerp_vec(self._cam_pos, target_pos, t * 2)
            self._cam_look = self._lerp_vec(self._cam_look, target_look, t * 2)
            
            cam.x, cam.y, cam.z = self._cam_pos
            
            gluLookAt(
                self._cam_pos[0], self._cam_pos[1], self._cam_pos[2],
                self._cam_look[0], self._cam_look[1], self._cam_look[2],
                0, 1, 0
            )
        else:
            # Manual camera control dengan smooth transition
            args = cam.look_at_args()
            target_pos = [args[0], args[1], args[2]]
            target_look = [args[3], args[4], args[5]]
            
            self._cam_pos = self._lerp_vec(self._cam_pos, target_pos, t * 4)
            self._cam_look = self._lerp_vec(self._cam_look, target_look, t * 4)
            
            gluLookAt(
                self._cam_pos[0], self._cam_pos[1], self._cam_pos[2],
                self._cam_look[0], self._cam_look[1], self._cam_look[2],
                0, 1, 0
            )
