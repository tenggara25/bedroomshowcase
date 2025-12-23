from OpenGL.GL import *
from src.geometry.primitives import draw_cube

class Desk:
    def __init__(self):
        self.visible = True
        self.pos = (2.0, 0.0, -1.2)
        self.top_w, self.top_h, self.top_d = 1.8, 0.10, 0.75
        self.leg_w, self.leg_h, self.leg_d = 0.10, 0.75, 0.10

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
