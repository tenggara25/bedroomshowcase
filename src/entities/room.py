from OpenGL.GL import *
from src.geometry.primitives import draw_textured_quad

class Room:
    def __init__(self):
        self.visible = True
        self.size = 8.0
        self.height = 3.0

    def update(self, dt, ctx):
        pass

    def _quad(self, v0, v1, v2, v3, n, uv=(1.0, 1.0)):
        su, sv = uv
        glBegin(GL_QUADS)
        glNormal3f(*n)
        glTexCoord2f(0.0, 0.0); glVertex3f(*v0)
        glTexCoord2f(su, 0.0);  glVertex3f(*v1)
        glTexCoord2f(su, sv);   glVertex3f(*v2)
        glTexCoord2f(0.0, sv);  glVertex3f(*v3)
        glEnd()

    def draw(self, ctx):
        tex = ctx["textures"]
        lighting = ctx["lighting"]
        mode = getattr(lighting, "mode", "day")

        S = self.size
        H = self.height
        hs = S / 2.0

        # --- Room surfaces ---
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)

        # Floor
        glBindTexture(GL_TEXTURE_2D, tex.load("floor.jpg"))
        draw_textured_quad(S, S, uv_scale=6.0)

        # Rug (karpet) di atas lantai (sedikit naik agar tidak z-fighting)
        glBindTexture(GL_TEXTURE_2D, tex.load("rug.jpg"))
        glPushMatrix()
        glTranslatef(0.0, 0.01, 0.3)  # y kecil
        draw_textured_quad(3.2, 2.2, uv_scale=1.0)
        glPopMatrix()

        # Ceiling
        glBindTexture(GL_TEXTURE_2D, tex.load("wall.jpg"))
        self._quad(
            (-hs, H, -hs), ( hs, H, -hs), ( hs, H,  hs), (-hs, H,  hs),
            (0.0, -1.0, 0.0), uv=(6.0, 6.0)
        )

        # Back wall (z=-hs)
        self._quad(
            (-hs, 0.0, -hs), ( hs, 0.0, -hs), ( hs, H, -hs), (-hs, H, -hs),
            (0.0, 0.0, 1.0), uv=(6.0, 3.0)
        )

        # Front wall (z=+hs)
        self._quad(
            ( hs, 0.0,  hs), (-hs, 0.0,  hs), (-hs, H,  hs), ( hs, H,  hs),
            (0.0, 0.0, -1.0), uv=(6.0, 3.0)
        )

        # Left wall (x=-hs)
        self._quad(
            (-hs, 0.0,  hs), (-hs, 0.0, -hs), (-hs, H, -hs), (-hs, H,  hs),
            (1.0, 0.0, 0.0), uv=(6.0, 3.0)
        )

        # Right wall (x=+hs)
        self._quad(
            ( hs, 0.0, -hs), ( hs, 0.0,  hs), ( hs, H,  hs), ( hs, H, -hs),
            (-1.0, 0.0, 0.0), uv=(6.0, 3.0)
        )

        # Poster di dinding kanan (x=+hs), sedikit keluar agar tidak z-fighting
        glBindTexture(GL_TEXTURE_2D, tex.load("poster.jpg"))
        x = hs - 0.01
        self._quad(
            (x, 1.0, -0.6), (x, 1.0, 0.6), (x, 2.2, 0.6), (x, 2.2, -0.6),
            (-1.0, 0.0, 0.0), uv=(1.0, 1.0)
        )

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)

        # --- Window panel (emissive-like) ---
        glPushAttrib(GL_ENABLE_BIT | GL_CURRENT_BIT)
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        if mode == "day":
            glColor4f(0.60, 0.80, 1.0, 0.75)
        else:
            glColor4f(0.10, 0.12, 0.20, 0.70)

        z = -hs + 0.02
        glBegin(GL_QUADS)
        glVertex3f(-1.2, 1.1, z)
        glVertex3f( 1.2, 1.1, z)
        glVertex3f( 1.2, 2.2, z)
        glVertex3f(-1.2, 2.2, z)
        glEnd()

        glPopAttrib()
