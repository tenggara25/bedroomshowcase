from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Wardrobe(Entity):
    """Lemari pakaian besar dengan pintu"""
    def __init__(self):
        super().__init__("Wardrobe")
        self.visible = True
        # Posisi di dinding kiri, dekat pintu
        self.pos = (-3.85, 0.0, 1.5)
        
        self.width = 1.2
        self.height = 2.2
        self.depth = 0.55
        
        self.is_open = False
        self.door_angle = 0.0
        self.target_angle = 0.0
        self.speed = 90.0

    def toggle(self):
        self.is_open = not self.is_open
        self.target_angle = 85.0 if self.is_open else 0.0

    def update(self, dt, ctx):
        if self.door_angle < self.target_angle:
            self.door_angle = min(self.target_angle, self.door_angle + self.speed * dt)
        elif self.door_angle > self.target_angle:
            self.door_angle = max(self.target_angle, self.door_angle - self.speed * dt)

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)
        
        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))

        # Main body (back panel)
        glColor3f(0.45, 0.32, 0.22)
        glPushMatrix()
        glTranslatef(self.pos[0], self.height/2, self.pos[2])
        glScalef(0.05, self.height, self.width)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Top panel
        glColor3f(0.5, 0.35, 0.25)
        glPushMatrix()
        glTranslatef(self.pos[0] + self.depth/2, self.height - 0.02, self.pos[2])
        glScalef(self.depth, 0.04, self.width)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Bottom panel
        glPushMatrix()
        glTranslatef(self.pos[0] + self.depth/2, 0.02, self.pos[2])
        glScalef(self.depth, 0.04, self.width)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Side panels
        glColor3f(0.48, 0.33, 0.23)
        # Left side
        glPushMatrix()
        glTranslatef(self.pos[0] + self.depth/2, self.height/2, self.pos[2] - self.width/2 + 0.02)
        glScalef(self.depth, self.height, 0.04)
        draw_cube(1, 1, 1)
        glPopMatrix()
        
        # Right side
        glPushMatrix()
        glTranslatef(self.pos[0] + self.depth/2, self.height/2, self.pos[2] + self.width/2 - 0.02)
        glScalef(self.depth, self.height, 0.04)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Shelves inside (visible when open)
        if self.door_angle > 20:
            glColor3f(0.52, 0.38, 0.28)
            for shelf_y in [0.5, 1.0, 1.5]:
                glPushMatrix()
                glTranslatef(self.pos[0] + self.depth/2, shelf_y, self.pos[2])
                glScalef(self.depth - 0.1, 0.02, self.width - 0.1)
                draw_cube(1, 1, 1)
                glPopMatrix()

        # Doors (2 pintu)
        door_width = (self.width - 0.04) / 2
        door_depth = 0.03
        
        # Left door
        glColor3f(0.55, 0.4, 0.28)
        glPushMatrix()
        glTranslatef(self.pos[0] + self.depth, self.height/2, self.pos[2] - door_width/2 - 0.01)
        # Hinge di sisi kiri
        glTranslatef(0, 0, -door_width/2)
        glRotatef(-self.door_angle, 0, 1, 0)
        glTranslatef(0, 0, door_width/2)
        glScalef(door_depth, self.height - 0.08, door_width)
        draw_cube(1, 1, 1)
        glPopMatrix()
        
        # Left door handle
        glColor3f(0.7, 0.6, 0.3)
        glPushMatrix()
        glTranslatef(self.pos[0] + self.depth + 0.02, self.height/2, self.pos[2] - 0.08)
        glTranslatef(0, 0, -door_width/2 - 0.01 + door_width/2)
        glTranslatef(0, 0, -door_width/2)
        glRotatef(-self.door_angle, 0, 1, 0)
        glTranslatef(0, 0, door_width/2)
        glTranslatef(0, 0, door_width/2 - 0.05)
        glScalef(0.02, 0.08, 0.02)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Right door
        glColor3f(0.55, 0.4, 0.28)
        glPushMatrix()
        glTranslatef(self.pos[0] + self.depth, self.height/2, self.pos[2] + door_width/2 + 0.01)
        # Hinge di sisi kanan
        glTranslatef(0, 0, door_width/2)
        glRotatef(self.door_angle, 0, 1, 0)
        glTranslatef(0, 0, -door_width/2)
        glScalef(door_depth, self.height - 0.08, door_width)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Right door handle
        glColor3f(0.7, 0.6, 0.3)
        glPushMatrix()
        glTranslatef(self.pos[0] + self.depth + 0.02, self.height/2, self.pos[2] + 0.08)
        glTranslatef(0, 0, door_width/2 + 0.01 - door_width/2)
        glTranslatef(0, 0, door_width/2)
        glRotatef(self.door_angle, 0, 1, 0)
        glTranslatef(0, 0, -door_width/2)
        glTranslatef(0, 0, -door_width/2 + 0.05)
        glScalef(0.02, 0.08, 0.02)
        draw_cube(1, 1, 1)
        glPopMatrix()

        glColor3f(1.0, 1.0, 1.0)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
