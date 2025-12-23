import math
from OpenGL.GL import *
from src.geometry.primitives import draw_cube

class Lamp:
    def __init__(self):
        self.visible = True
        self.pos = (0.0, 2.55, 0.0)
        self.t = 0.0
        self.base = 0.90
        self.amp = 0.20
        self.freq = 1.2

    def update(self, dt, ctx):
        self.t += dt
        lighting = ctx["lighting"]

        if lighting.enabled:
            wave = 0.5 * (1.0 + math.sin(self.t * (2.0 * math.pi) * self.freq))
            lighting.intensity = self.base + self.amp * wave
        else:
            lighting.intensity = 1.0

    def draw(self, ctx):
        tex = ctx["textures"]
        lighting = ctx["lighting"]

        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)

        # housing
        glBindTexture(GL_TEXTURE_2D, tex.load("wall.jpg"))
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glScalef(0.35, 0.12, 0.35)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # bulb (bright)
        glPushAttrib(GL_ENABLE_BIT)
        glDisable(GL_LIGHTING)
        b = 0.2 if not lighting.enabled else min(1.0, 0.6 + 0.4 * (lighting.intensity / (self.base + self.amp)))
        glColor3f(b, b, b)
        glBindTexture(GL_TEXTURE_2D, 0)

        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] - 0.08, self.pos[2])
        glScalef(0.18, 0.10, 0.18)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glPopAttrib()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
