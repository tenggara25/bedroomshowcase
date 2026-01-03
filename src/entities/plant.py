from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity
import math

class Plant(Entity):
    """Tanaman hias dalam pot"""
    def __init__(self):
        super().__init__("Plant")
        self.visible = True
        # Posisi di pojok kamar
        self.pos = (3.2, 0.0, 2.8)
        self.sway_time = 0.0

    def update(self, dt, ctx):
        self.sway_time += dt

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        
        # Pot (coklat kemerahan)
        glColor3f(0.6, 0.35, 0.2)
        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))
        
        # Pot bawah
        glPushMatrix()
        glTranslatef(self.pos[0], 0.12, self.pos[2])
        glScalef(0.3, 0.24, 0.3)
        draw_cube(1, 1, 1)
        glPopMatrix()
        
        # Pot rim (bibir pot)
        glColor3f(0.55, 0.3, 0.18)
        glPushMatrix()
        glTranslatef(self.pos[0], 0.26, self.pos[2])
        glScalef(0.35, 0.04, 0.35)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Tanah
        glColor3f(0.25, 0.15, 0.1)
        glPushMatrix()
        glTranslatef(self.pos[0], 0.25, self.pos[2])
        glScalef(0.28, 0.02, 0.28)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, 0)
        
        # Batang utama (hijau tua)
        glColor3f(0.2, 0.4, 0.15)
        glPushMatrix()
        glTranslatef(self.pos[0], 0.45, self.pos[2])
        glScalef(0.03, 0.4, 0.03)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Daun-daun (hijau dengan sedikit sway)
        sway = math.sin(self.sway_time * 2) * 0.02
        
        leaves = [
            (0.0, 0.5, 0.0, 0.0),
            (0.08, 0.45, 0.05, 15),
            (-0.08, 0.48, -0.05, -15),
            (0.05, 0.55, -0.08, 10),
            (-0.06, 0.52, 0.07, -12),
            (0.0, 0.6, 0.06, 8),
            (0.07, 0.58, 0.0, -8),
        ]
        
        for ox, oy, oz, angle in leaves:
            glColor3f(0.25 + ox*0.5, 0.55 + oy*0.2, 0.2)
            glPushMatrix()
            glTranslatef(self.pos[0] + ox + sway, oy, self.pos[2] + oz)
            glRotatef(angle + sway * 100, 0, 0, 1)
            glScalef(0.15, 0.02, 0.08)
            draw_cube(1, 1, 1)
            glPopMatrix()

        glColor3f(1.0, 1.0, 1.0)
        glDisable(GL_TEXTURE_2D)
