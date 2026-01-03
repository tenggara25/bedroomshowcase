from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Desk(Entity):
    def __init__(self):
        super().__init__("Desk")
        self.visible = True
        # Posisi desk: sisi kanan kamar, menghadap dinding
        self.pos = (3.2, 0.0, -2.0)
        self.top_w, self.top_h, self.top_d = 1.4, 0.08, 0.65
        self.leg_w, self.leg_h, self.leg_d = 0.08, 0.72, 0.08

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)

        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))

        # Top
        glPushMatrix()
        glTranslatef(self.pos[0], 0.85, self.pos[2])
        glScalef(self.top_w, self.top_h, self.top_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Legs
        leg_y = 0.85 - (self.top_h * 0.5) - (self.leg_h * 0.5)
        offsets = [
            (-self.top_w*0.5 + self.leg_w*0.5, leg_y, -self.top_d*0.5 + self.leg_d*0.5),
            ( self.top_w*0.5 - self.leg_w*0.5, leg_y, -self.top_d*0.5 + self.leg_d*0.5),
            (-self.top_w*0.5 + self.leg_w*0.5, leg_y,  self.top_d*0.5 - self.leg_d*0.5),
            ( self.top_w*0.5 - self.leg_w*0.5, leg_y,  self.top_d*0.5 - self.leg_d*0.5),
        ]
        for ox, oy, oz in offsets:
            glPushMatrix()
            glTranslatef(self.pos[0] + ox, oy, self.pos[2] + oz)
            glScalef(self.leg_w, self.leg_h, self.leg_d)
            draw_cube(1, 1, 1)
            glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
