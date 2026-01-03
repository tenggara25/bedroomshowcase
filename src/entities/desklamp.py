from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class DeskLamp(Entity):
    """Lampu meja di atas nightstand dengan toggle on/off"""
    def __init__(self):
        super().__init__("DeskLamp")
        self.visible = True
        # Posisi di atas nightstand
        self.pos = (-1.2, 0.6, -2.2)
        self.is_on = False
        
    def toggle(self):
        self.is_on = not self.is_on

    def update(self, dt, ctx):
        # Update desk lamp light di lighting
        lighting = ctx["lighting"]
        lighting.desk_lamp_on = self.is_on

    def draw(self, ctx):
        tex = ctx["textures"]
        lighting = ctx["lighting"]
        
        glEnable(GL_TEXTURE_2D)
        
        # Base lampu (hitam)
        glColor3f(0.15, 0.15, 0.15)
        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], self.pos[2])
        glScalef(0.12, 0.03, 0.12)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Tiang lampu
        glColor3f(0.3, 0.3, 0.3)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + 0.12, self.pos[2])
        glScalef(0.02, 0.2, 0.02)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Kap lampu (cone shape approximation)
        glColor3f(0.9, 0.85, 0.7)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + 0.25, self.pos[2])
        glScalef(0.12, 0.1, 0.12)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Bulb (menyala jika on)
        glPushAttrib(GL_ENABLE_BIT)
        glDisable(GL_LIGHTING)
        
        if self.is_on and lighting.mode == "night":
            glColor3f(1.0, 0.95, 0.7)  # Warm yellow
        else:
            glColor3f(0.3, 0.3, 0.25)  # Off
        
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + 0.2, self.pos[2])
        glScalef(0.05, 0.06, 0.05)
        draw_cube(1, 1, 1)
        glPopMatrix()
        
        glPopAttrib()

        glColor3f(1.0, 1.0, 1.0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
