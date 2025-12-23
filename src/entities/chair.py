from OpenGL.GL import *
from src.geometry.primitives import draw_cube

class Chair:
    def __init__(self):
        self.visible = True
        self.pos = (1.6, 0.0, -0.9)
        self.seat_w, self.seat_h, self.seat_d = 0.55, 0.08, 0.55
        self.leg_w, self.leg_h, self.leg_d = 0.08, 0.45, 0.08
        self.back_w, self.back_h, self.back_d = 0.55, 0.55, 0.08

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)

        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))

        # Seat
        glPushMatrix()
        glTranslatef(self.pos[0], 0.55, self.pos[2])
        glScalef(self.seat_w, self.seat_h, self.seat_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Legs
        leg_y = 0.55 - (self.seat_h * 0.5) - (self.leg_h * 0.5)
        offsets = [
            (-self.seat_w*0.5 + self.leg_w*0.5, leg_y, -self.seat_d*0.5 + self.leg_d*0.5),
            ( self.seat_w*0.5 - self.leg_w*0.5, leg_y, -self.seat_d*0.5 + self.leg_d*0.5),
            (-self.seat_w*0.5 + self.leg_w*0.5, leg_y,  self.seat_d*0.5 - self.leg_d*0.5),
            ( self.seat_w*0.5 - self.leg_w*0.5, leg_y,  self.seat_d*0.5 - self.leg_d*0.5),
        ]
        for ox, oy, oz in offsets:
            glPushMatrix()
            glTranslatef(self.pos[0] + ox, oy, self.pos[2] + oz)
            glScalef(self.leg_w, self.leg_h, self.leg_d)
            draw_cube(1, 1, 1)
            glPopMatrix()

        # Backrest
        glPushMatrix()
        glTranslatef(
            self.pos[0],
            0.55 + (self.back_h * 0.5),
            self.pos[2] - (self.seat_d * 0.5) + (self.back_d * 0.5),
        )
        glScalef(self.back_w, self.back_h, self.back_d)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
