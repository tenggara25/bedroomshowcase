from OpenGL.GL import *
from OpenGL.GLU import *

class Renderer:
    def __init__(self):
        self.auto_tour = True
        self.focus_target = None
        self.focus_name = None
        self._t = 0.0

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

    def apply_camera(self, cam, dt):
        import math
        if self.focus_target:
            gluLookAt(cam.x, cam.y, cam.z,
                      *self.focus_target, 0,1,0)
            return

        if self.auto_tour:
            self._t += dt
            r = 2.8
            cam.x = math.cos(self._t*0.4)*r
            cam.z = math.sin(self._t*0.4)*r
            cam.y = 1.8
            gluLookAt(cam.x, cam.y, cam.z, 0,1.2,0, 0,1,0)
        else:
            gluLookAt(*cam.look_at_args())
