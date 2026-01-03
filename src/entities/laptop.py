from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Laptop(Entity):
    def __init__(self):
        super().__init__("Laptop")
        self.visible = True
        # Posisi di atas meja (sesuai desk position)
        self.pos = (3.2, 0.82, -2.0)
        self.screen_angle = 110.0  # sudut layar terbuka

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        
        # Base laptop (keyboard area) - warna abu gelap
        glColor3f(0.15, 0.15, 0.18)
        glBindTexture(GL_TEXTURE_2D, tex.load("wall.jpg"))
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glScalef(0.4, 0.025, 0.28)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Keyboard area (sedikit lebih terang)
        glColor3f(0.1, 0.1, 0.12)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + 0.015, self.pos[2] + 0.02)
        glScalef(0.35, 0.008, 0.18)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Touchpad
        glColor3f(0.12, 0.12, 0.14)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + 0.015, self.pos[2] + 0.1)
        glScalef(0.1, 0.006, 0.06)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Screen (layar) - dengan rotasi
        glPushMatrix()
        # Pindah ke engsel (belakang laptop)
        glTranslatef(self.pos[0], self.pos[1] + 0.012, self.pos[2] - 0.13)
        # Rotasi layar
        glRotatef(-self.screen_angle + 90, 1.0, 0.0, 0.0)
        # Frame layar
        glColor3f(0.15, 0.15, 0.18)
        glTranslatef(0, 0.14, 0)
        glScalef(0.4, 0.28, 0.015)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Screen display (bagian dalam layar - menyala)
        glPushAttrib(GL_ENABLE_BIT)
        glDisable(GL_LIGHTING)
        
        lighting = ctx["lighting"]
        if lighting.mode == "night":
            glColor3f(0.3, 0.5, 0.7)  # Layar menyala biru malam
        else:
            glColor3f(0.7, 0.8, 0.9)  # Layar terang siang
        
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + 0.012, self.pos[2] - 0.13)
        glRotatef(-self.screen_angle + 90, 1.0, 0.0, 0.0)
        glTranslatef(0, 0.14, 0.01)
        glScalef(0.36, 0.24, 0.005)
        draw_cube(1, 1, 1)
        glPopMatrix()
        
        glPopAttrib()

        glColor3f(1.0, 1.0, 1.0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
