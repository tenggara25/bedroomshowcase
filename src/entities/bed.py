from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Bed(Entity):
    def __init__(self):
        super().__init__("Bed")
        self.visible = True

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)

        # Posisi bed: pojok kiri belakang kamar
        bx, bz = -2.5, -2.5

        # Base kayu (frame tempat tidur)
        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))
        glPushMatrix()
        glTranslatef(bx, 0.25, bz)
        glScalef(2.0, 0.5, 1.2)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Headboard (sandaran kepala) - di sisi dinding kiri
        glPushMatrix()
        glTranslatef(-3.85, 0.7, bz)
        glScalef(0.1, 1.0, 1.2)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Kasur (mattress) - warna putih/krem
        glColor3f(0.95, 0.93, 0.88)
        glBindTexture(GL_TEXTURE_2D, tex.load("wall.jpg"))
        glPushMatrix()
        glTranslatef(bx, 0.55, bz)
        glScalef(1.9, 0.15, 1.1)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Sprei (bed sheet) - warna biru muda
        glColor3f(0.7, 0.8, 0.9)
        glPushMatrix()
        glTranslatef(bx, 0.65, bz)
        glScalef(1.92, 0.04, 1.12)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Bantal 1 - putih
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        glTranslatef(-3.4, 0.75, bz - 0.3)
        glScalef(0.35, 0.12, 0.4)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Bantal 2 - putih
        glPushMatrix()
        glTranslatef(-3.4, 0.75, bz + 0.3)
        glScalef(0.35, 0.12, 0.4)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Selimut - warna merah marun terlipat di kaki kasur
        glColor3f(0.5, 0.15, 0.2)
        glBindTexture(GL_TEXTURE_2D, tex.load("rug.jpg"))
        glPushMatrix()
        glTranslatef(bx + 0.7, 0.7, bz)
        glScalef(0.5, 0.08, 1.0)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glColor3f(1.0, 1.0, 1.0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
