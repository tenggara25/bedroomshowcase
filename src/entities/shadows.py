from OpenGL.GL import *
from src.entities.base import Entity

class Shadows(Entity):
    """Fake shadows di bawah objek utama"""
    def __init__(self):
        super().__init__("Shadows")
        self.visible = True
        
        # Shadow positions and sizes [x, z, width, depth]
        self.shadows = [
            # Bed shadow
            {"pos": (-2.5, -2.5), "size": (2.2, 1.4), "alpha": 0.25},
            # Desk shadow
            {"pos": (3.2, -2.0), "size": (1.5, 0.7), "alpha": 0.2},
            # Chair shadow
            {"pos": (2.3, -2.0), "size": (0.5, 0.5), "alpha": 0.15},
            # Nightstand shadow
            {"pos": (-1.2, -2.5), "size": (0.55, 0.5), "alpha": 0.15},
            # Bookshelf shadow
            {"pos": (1.0, -3.7), "size": (1.1, 0.35), "alpha": 0.2},
            # Plant shadow
            {"pos": (3.2, 2.8), "size": (0.4, 0.4), "alpha": 0.15},
            # Wardrobe shadow
            {"pos": (-3.6, 1.5), "size": (0.6, 1.3), "alpha": 0.25},
        ]

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        lighting = ctx["lighting"]
        
        # Shadows lebih terlihat saat siang
        base_alpha = 0.3 if lighting.mode == "day" else 0.15
        
        glPushAttrib(GL_ENABLE_BIT | GL_CURRENT_BIT)
        glDisable(GL_LIGHTING)
        glDisable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        y = 0.005  # Slightly above floor to prevent z-fighting
        
        for shadow in self.shadows:
            x, z = shadow["pos"]
            w, d = shadow["size"]
            alpha = shadow["alpha"] * (base_alpha / 0.2)
            
            glColor4f(0.0, 0.0, 0.0, alpha)
            
            # Draw shadow as quad with soft edges (simple version)
            glBegin(GL_QUADS)
            glVertex3f(x - w/2, y, z - d/2)
            glVertex3f(x + w/2, y, z - d/2)
            glVertex3f(x + w/2, y, z + d/2)
            glVertex3f(x - w/2, y, z + d/2)
            glEnd()
        
        glPopAttrib()
