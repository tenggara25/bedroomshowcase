from OpenGL.GL import *
from src import config

class Lighting:
    def __init__(self):
        self.enabled = True
        self.intensity = 1.0
        self.mode = "day"

    def toggle_mode(self):
        self.mode = "night" if self.mode == "day" else "day"

    def apply(self):
        if not self.enabled:
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            return

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)

        if self.mode == "day":
            amb0, dif0 = (0.3,0.3,0.3,1), (0.9,0.9,0.9,1)
            amb1, dif1 = (0.2,0.25,0.35,1), (0.6,0.7,0.9,1)
        else:
            amb0, dif0 = (0.1,0.1,0.15,1), (0.7,0.7,0.8,1)
            amb1, dif1 = (0.03,0.04,0.06,1), (0.1,0.1,0.15,1)

        glLightfv(GL_LIGHT0, GL_POSITION, config.LIGHT_POS)
        glLightfv(GL_LIGHT0, GL_AMBIENT, amb0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, dif0)

        glLightfv(GL_LIGHT1, GL_POSITION, (0, 2.0, -3.8, 1))
        glLightfv(GL_LIGHT1, GL_AMBIENT, amb1)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, dif1)
