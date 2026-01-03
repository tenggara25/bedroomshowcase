from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Chair(Entity):
    def __init__(self):
        super().__init__("Chair")
        self.visible = True
        # Posisi chair: di depan desk, menghadap desk
        self.pos = (2.3, 0.0, -2.0)
        self.seat_w, self.seat_h, self.seat_d = 0.45, 0.06, 0.45
        self.leg_w, self.leg_h, self.leg_d = 0.06, 0.42, 0.06
        self.back_w, self.back_h, self.back_d = 0.45, 0.5, 0.06

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
