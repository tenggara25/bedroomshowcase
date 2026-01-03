from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Lamp(Entity):
    """Lampu plafon utama"""
    def __init__(self):
        super().__init__("Lamp")
        self.visible = True
        self.pos = (0.0, 2.55, 0.0)

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        tex = ctx["textures"]
        lighting = ctx["lighting"]

        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)

        # Housing
        glBindTexture(GL_TEXTURE_2D, tex.load("wall.jpg"))
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glScalef(0.35, 0.12, 0.35)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Bulb
        glPushAttrib(GL_ENABLE_BIT)
        glDisable(GL_LIGHTING)
        
        if lighting.enabled and lighting.mode == "day":
            glColor3f(1.0, 0.98, 0.9)  # Bright
        else:
            glColor3f(0.3, 0.3, 0.25)  # Dim
        
        glBindTexture(GL_TEXTURE_2D, 0)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] - 0.08, self.pos[2])
        glScalef(0.18, 0.10, 0.18)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glPopAttrib()
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
