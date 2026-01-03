from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Door(Entity):
    def __init__(self):
        super().__init__("Door")
        self.visible = True
        
        # Posisi pintu di dinding depan (z = +hs)
        self.pos = (-2.0, 0.0, 3.99)
        
        self.frame_w = 0.95
        self.frame_h = 2.1
        self.frame_d = 0.12
        self.door_w = 0.85
        self.door_h = 2.0
        self.door_d = 0.05
        
        self.is_open = False
        self.angle = 0.0
        self.target_angle = 0.0
        self.speed = 120.0

    def toggle(self):
        self.is_open = not self.is_open
        self.target_angle = -90.0 if self.is_open else 0.0

    def update(self, dt, ctx):
        if self.angle < self.target_angle:
            self.angle = min(self.target_angle, self.angle + self.speed * dt)
        elif self.angle > self.target_angle:
            self.angle = max(self.target_angle, self.angle - self.speed * dt)

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)
        
        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))

        # Door Frame - Left
        glColor3f(0.85, 0.75, 0.65)
        glPushMatrix()
        glTranslatef(self.pos[0] - self.frame_w/2 + 0.05, self.frame_h/2, self.pos[2])
        glScalef(0.1, self.frame_h, self.frame_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Door Frame - Right
        glPushMatrix()
        glTranslatef(self.pos[0] + self.frame_w/2 - 0.05, self.frame_h/2, self.pos[2])
        glScalef(0.1, self.frame_h, self.frame_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Door Frame - Top
        glPushMatrix()
        glTranslatef(self.pos[0], self.frame_h - 0.05, self.pos[2])
        glScalef(self.frame_w, 0.1, self.frame_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Door panel dengan animasi rotasi
        glColor3f(0.55, 0.4, 0.3)
        glPushMatrix()
        glTranslatef(self.pos[0], self.door_h/2, self.pos[2])
        
        # Hinge di sisi kiri
        hinge_x = -self.door_w / 2
        glTranslatef(hinge_x, 0.0, 0.0)
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        glTranslatef(-hinge_x, 0.0, 0.0)
        
        glScalef(self.door_w, self.door_h, self.door_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Door handle
        glColor3f(0.8, 0.7, 0.2)  # Warna kuningan
        glPushMatrix()
        glTranslatef(self.pos[0], self.door_h/2, self.pos[2])
        
        # Ikut rotasi pintu
        glTranslatef(hinge_x, 0.0, 0.0)
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        glTranslatef(-hinge_x, 0.0, 0.0)
        
        # Handle position
        glTranslatef(self.door_w/2 - 0.12, 0.0, self.door_d/2 + 0.02)
        glScalef(0.08, 0.03, 0.04)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glColor3f(1.0, 1.0, 1.0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
