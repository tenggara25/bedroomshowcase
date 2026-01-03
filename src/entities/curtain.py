from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Curtain(Entity):
    """Tirai di samping jendela"""
    def __init__(self):
        super().__init__("Curtain")
        self.visible = True
        
        # Window position (di dinding belakang)
        self.window_x = 0.0
        self.window_y_bottom = 1.1
        self.window_y_top = 2.2
        self.window_z = -3.98
        
        # Curtain dimensions
        self.curtain_width = 0.4
        self.curtain_height = 1.3

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        tex = ctx["textures"]
        lighting = ctx["lighting"]
        
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, tex.load("rug.jpg"))
        
        # Curtain rod (batang gorden)
        glColor3f(0.6, 0.5, 0.3)
        glPushMatrix()
        glTranslatef(self.window_x, self.window_y_top + 0.15, self.window_z + 0.05)
        glScalef(3.0, 0.04, 0.04)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Rod finials (ujung batang)
        glColor3f(0.65, 0.55, 0.35)
        for x_off in [-1.55, 1.55]:
            glPushMatrix()
            glTranslatef(self.window_x + x_off, self.window_y_top + 0.15, self.window_z + 0.05)
            glScalef(0.06, 0.06, 0.06)
            draw_cube(1, 1, 1)
            glPopMatrix()

        # Warna tirai berdasarkan mode
        if lighting.mode == "day":
            glColor3f(0.8, 0.7, 0.6)  # Krem terang
        else:
            glColor3f(0.5, 0.4, 0.35)  # Gelap
        
        # Left curtain
        glPushMatrix()
        glTranslatef(self.window_x - 1.0, self.window_y_bottom + self.curtain_height/2, self.window_z + 0.03)
        glScalef(self.curtain_width, self.curtain_height, 0.02)
        draw_cube(1, 1, 1)
        glPopMatrix()
        
        # Left curtain folds
        for i in range(3):
            glPushMatrix()
            glTranslatef(self.window_x - 1.0 + 0.12 + i*0.08, 
                        self.window_y_bottom + self.curtain_height/2, 
                        self.window_z + 0.04)
            glScalef(0.03, self.curtain_height - 0.1, 0.01)
            draw_cube(1, 1, 1)
            glPopMatrix()

        # Right curtain
        glPushMatrix()
        glTranslatef(self.window_x + 1.0, self.window_y_bottom + self.curtain_height/2, self.window_z + 0.03)
        glScalef(self.curtain_width, self.curtain_height, 0.02)
        draw_cube(1, 1, 1)
        glPopMatrix()
        
        # Right curtain folds
        for i in range(3):
            glPushMatrix()
            glTranslatef(self.window_x + 1.0 - 0.12 - i*0.08, 
                        self.window_y_bottom + self.curtain_height/2, 
                        self.window_z + 0.04)
            glScalef(0.03, self.curtain_height - 0.1, 0.01)
            draw_cube(1, 1, 1)
            glPopMatrix()

        glColor3f(1.0, 1.0, 1.0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
