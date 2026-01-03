from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity
import math

class CeilingFan(Entity):
    """Kipas angin langit-langit dengan animasi berputar"""
    def __init__(self):
        super().__init__("CeilingFan")
        self.visible = True
        self.pos = (0.0, 2.85, 0.0)
        self.rotation = 0.0
        self.speed = 180.0  # degrees per second
        self.is_on = True
        self.blade_count = 4

    def toggle(self):
        self.is_on = not self.is_on

    def update(self, dt, ctx):
        if self.is_on:
            self.rotation += self.speed * dt
            if self.rotation >= 360:
                self.rotation -= 360

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        
        # Motor housing (tengah)
        glColor3f(0.85, 0.85, 0.85)
        glBindTexture(GL_TEXTURE_2D, tex.load("wall.jpg"))
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glScalef(0.2, 0.12, 0.2)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Rod (tiang penghubung ke ceiling)
        glColor3f(0.7, 0.7, 0.7)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + 0.1, self.pos[2])
        glScalef(0.04, 0.15, 0.04)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Ceiling mount
        glColor3f(0.8, 0.8, 0.8)
        glPushMatrix()
        glTranslatef(self.pos[0], 2.98, self.pos[2])
        glScalef(0.12, 0.04, 0.12)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))
        
        # Blades dengan rotasi
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] - 0.02, self.pos[2])
        glRotatef(self.rotation, 0, 1, 0)
        
        for i in range(self.blade_count):
            angle = i * (360 / self.blade_count)
            glPushMatrix()
            glRotatef(angle, 0, 1, 0)
            
            # Blade
            glColor3f(0.45, 0.3, 0.2)
            glPushMatrix()
            glTranslatef(0.4, 0, 0)
            glScalef(0.6, 0.02, 0.12)
            draw_cube(1, 1, 1)
            glPopMatrix()
            
            # Blade holder
            glColor3f(0.6, 0.6, 0.6)
            glPushMatrix()
            glTranslatef(0.08, 0.01, 0)
            glScalef(0.08, 0.025, 0.04)
            draw_cube(1, 1, 1)
            glPopMatrix()
            
            glPopMatrix()
        
        glPopMatrix()

        glColor3f(1.0, 1.0, 1.0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
