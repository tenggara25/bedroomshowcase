from OpenGL.GLUT import *
from OpenGL.GL import glViewport

from src import config
from src.time import Time
from src.input import InputState
from src.camera import Camera
from src.textures import TextureManager
from src.lighting import Lighting
from src.renderer import Renderer
from src.scene.bedroom_scene import BedroomScene

class Application:
    def __init__(self):
        self.time = Time()
        self.input = InputState()
        self.camera = Camera()
        self.renderer = Renderer()
        self.lighting = Lighting()
        self.textures = TextureManager(config.ASSET_TEX_DIR)
        self.win_w = config.WIN_WIDTH
        self.win_h = config.WIN_HEIGHT


        self.ctx = {
            "input": self.input,
            "camera": self.camera,
            "renderer": self.renderer,
            "lighting": self.lighting,
            "textures": self.textures,
        }

        self.scene = BedroomScene(self.ctx)
        self._last_mouse_x = None
        self._last_mouse_y = None

    def run(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(config.WIN_WIDTH, config.WIN_HEIGHT)
        glutCreateWindow(config.APP_TITLE.encode("utf-8"))

        self.renderer.init_gl()
        self.renderer.set_projection(config.WIN_WIDTH, config.WIN_HEIGHT)

        glutDisplayFunc(self._display)
        glutIdleFunc(self._idle)
        glutReshapeFunc(self._reshape)
        glutKeyboardFunc(self._key_down)
        glutKeyboardUpFunc(self._key_up)
        glutPassiveMotionFunc(self._mouse_move)

        glutMainLoop()

    def _reshape(self, w, h):
        glViewport(0, 0, w, h)
        self.renderer.set_projection(w, h)

    def _key_down(self, key, x, y):
        self.input.set_key(key, True)
        if key == b'\x1b':
            raise SystemExit
        self.scene.on_key(key, True)

    def _key_up(self, key, x, y):
        self.input.set_key(key, False)
        self.scene.on_key(key, False)

    def _mouse_move(self, x, y):
        if not self.input.mouse_captured:
            return
        if self._last_mouse_x is None:
            self._last_mouse_x, self._last_mouse_y = x, y
            return
        dx = x - self._last_mouse_x
        dy = y - self._last_mouse_y
        self._last_mouse_x, self._last_mouse_y = x, y
        self.input.mouse_dx += dx
        self.input.mouse_dy += dy

    def _idle(self):
        glutPostRedisplay()

    def _update_camera_controls(self, dt):
        if self.renderer.auto_tour:
            self.input.reset_mouse_delta()
            return

        self.camera.update_mouse(self.input.mouse_dx, self.input.mouse_dy)
        self.input.reset_mouse_delta()

        forward = 0.0
        right = 0.0
        if self.input.is_down(b'w') or self.input.is_down(b'W'):
            forward += 1.0
        if self.input.is_down(b's') or self.input.is_down(b'S'):
            forward -= 1.0
        if self.input.is_down(b'd') or self.input.is_down(b'D'):
            right += 1.0
        if self.input.is_down(b'a') or self.input.is_down(b'A'):
            right -= 1.0

        self.camera.move(forward, right, dt)

    def _display(self):
        dt = self.time.tick()
        self._update_camera_controls(dt)

        self.renderer.begin_frame(self.lighting)   # <-- sebelumnya begin_frame()        self.lighting.apply()
        self.lighting.apply()
        self.renderer.apply_camera(self.camera, dt)

        self.scene.update(dt)
        self.scene.draw()

        glutSwapBuffers()
    def _display(self):
        dt = self.time.tick()
        self._update_camera_controls(dt)

        self.renderer.begin_frame(self.lighting)
        self.lighting.apply()
        self.renderer.apply_camera(self.camera, dt)

        self.scene.update(dt)
        self.scene.draw()

        if hasattr(self.scene, "hud"):
            self.scene.hud.draw_2d(self.ctx, self.win_w, self.win_h)

        glutSwapBuffers()
