from OpenGL.GL import *

class Lighting:
    def __init__(self):
        self.enabled = True
        self.mode = "day"
        
        # Lamp positions
        self.lamp_pos = (0.0, 2.5, 0.0, 1.0)
        self.desk_lamp_pos = (-1.2, 0.85, -2.2, 1.0)  # Di atas nightstand
        self.desk_lamp_on = False

    def toggle_mode(self):
        self.mode = "night" if self.mode == "day" else "day"

    def apply(self):
        if not self.enabled:
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glDisable(GL_LIGHT2)
            return

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)

        # Lighting setup: day/night mode with more dramatic and realistic values
        if self.mode == "day":
            amb0 = (0.35, 0.35, 0.38, 1.0)  # ambient utama lebih terang
            dif0 = (0.95, 0.95, 0.92, 1.0)  # diffuse utama lebih soft
            spec0 = (1.0, 1.0, 0.95, 1.0)   # specular utama
            amb1 = (0.18, 0.22, 0.32, 1.0)  # ambient sekunder
            dif1 = (0.55, 0.65, 0.85, 1.0)  # diffuse sekunder
            spec1 = (0.7, 0.8, 1.0, 1.0)    # specular sekunder
        else:
            amb0 = (0.08, 0.09, 0.13, 1.0)
            dif0 = (0.35, 0.38, 0.45, 1.0)
            spec0 = (0.3, 0.3, 0.4, 1.0)
            amb1 = (0.01, 0.02, 0.04, 1.0)
            dif1 = (0.08, 0.10, 0.18, 1.0)
            spec1 = (0.1, 0.12, 0.18, 1.0)

        # Light 0 (utama - ceiling lamp)
        glLightfv(GL_LIGHT0, GL_POSITION, self.lamp_pos)
        glLightfv(GL_LIGHT0, GL_AMBIENT, amb0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, dif0)
        glLightfv(GL_LIGHT0, GL_SPECULAR, spec0)
        
        # Attenuation untuk ceiling lamp (point light effect)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.09)
        glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.032)

        # Light 1 (sekunder - window light)
        glLightfv(GL_LIGHT1, GL_POSITION, (0, 2.0, -3.8, 1))
        glLightfv(GL_LIGHT1, GL_AMBIENT, amb1)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, dif1)
        glLightfv(GL_LIGHT1, GL_SPECULAR, spec1)

        # Light 2 (desk lamp - point light)
        if self.desk_lamp_on and self.mode == "night":
            glEnable(GL_LIGHT2)
            glLightfv(GL_LIGHT2, GL_POSITION, self.desk_lamp_pos)
            glLightfv(GL_LIGHT2, GL_AMBIENT, (0.1, 0.08, 0.05, 1.0))
            glLightfv(GL_LIGHT2, GL_DIFFUSE, (0.9, 0.75, 0.5, 1.0))  # Warm light
            glLightfv(GL_LIGHT2, GL_SPECULAR, (1.0, 0.9, 0.7, 1.0))
            
            # Point light attenuation (jarak dekat lebih terang)
            glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 1.0)
            glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.35)
            glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 0.44)
        else:
            glDisable(GL_LIGHT2)

        # Tambahan: material global agar permukaan lebih mengkilap
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.7, 0.7, 0.7, 1.0))
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 64.0)
