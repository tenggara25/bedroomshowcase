from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Drawer(Entity):
    def __init__(self):
        super().__init__("Drawer")
        self.visible = True
        # Posisi drawer: nightstand di samping bed
        self.pos = (-1.2, 0.0, -2.5)

        self.body_w, self.body_h, self.body_d = 0.5, 0.6, 0.45
        self.door_w, self.door_h, self.door_d = 0.48, 0.55, 0.03

        self.is_open = False
        self.angle = 0.0
        self.target_angle = 0.0
        self.speed = 160.0

    def toggle(self):
        self.is_open = not self.is_open
        self.target_angle = 70.0 if self.is_open else 0.0

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

        # Body
        glPushMatrix()
        glTranslatef(self.pos[0], self.body_h * 0.5, self.pos[2])
        glScalef(self.body_w, self.body_h, self.body_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Door with hinge rotation
        door_center_y = self.body_h * 0.5
        door_center_z = self.pos[2] + (self.body_d * 0.5) + (self.door_d * 0.5) - 0.01

        glPushMatrix()
        glTranslatef(self.pos[0], door_center_y, door_center_z)

        hinge_x = -self.door_w * 0.5
        glTranslatef(hinge_x, 0.0, 0.0)
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        glTranslatef(-hinge_x, 0.0, 0.0)

        glScalef(self.door_w, self.door_h, self.door_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
