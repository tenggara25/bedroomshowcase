from OpenGL.GL import *
from src.geometry.primitives import draw_cube

class Bed:
    def __init__(self):
        self.visible = True

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)

        # Base kayu
        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))
        glPushMatrix()
        glTranslatef(-2.0, 0.35, 1.6)
        glScalef(2.2, 0.7, 1.4)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Kasur
        glBindTexture(GL_TEXTURE_2D, tex.load("bed.jpg"))
        glPushMatrix()
        glTranslatef(-2.0, 0.85, 1.6)
        glScalef(2.1, 0.35, 1.3)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
