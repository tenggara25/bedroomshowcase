from OpenGL.GL import *
from src.geometry.primitives import draw_textured_quad


class Room:
    def __init__(self):
        self.visible = True
        self.size = 8.0
        self.height = 3.0
        # tanpa openGL call dlu

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

        # =====================================================
        # AMAN: OpenGL context SUDAH AKTIF
        # =====================================================
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)

        mode = getattr(lighting, "mode", "day")       # day / night
        lamp_on = getattr(lighting, "enabled", True) # lamp toggle

        S = self.size
        H = self.height
        hs = S / 2.0

        # =====================================================
        # OUTSIDE BACKGROUND (TIDAK TERPENGARUH LIGHTING)
        # =====================================================
        glPushAttrib(GL_ENABLE_BIT | GL_DEPTH_BUFFER_BIT)

        glDisable(GL_LIGHTING)
        glDisable(GL_DEPTH_TEST)

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, tex.load("outside.jpg"))
        glColor3f(1.0, 1.0, 1.0)

        z_out = -hs - 3.0
        self._quad(
            (-20.0, 0.0,  z_out),
            ( 20.0, 0.0,  z_out),
            ( 20.0, 15.0, z_out),
            (-20.0, 15.0, z_out),
            (0.0, 0.0, 1.0),
            uv=(4.0, 3.0)
        )

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
        glPopAttrib()

        # =====================================================
        # LIGHTING LOGIC (TIDAK TERBALIK)
        # =====================================================
        glEnable(GL_LIGHTING)

        if mode == "day":
            glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
            glLightfv(GL_LIGHT0, GL_AMBIENT, (0.45, 0.45, 0.45, 1.0))
        else:
            if lamp_on:
                glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.85, 0.80, 0.65, 1.0))
                glLightfv(GL_LIGHT0, GL_AMBIENT, (0.15, 0.15, 0.15, 1.0))
            else:
                glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.15, 0.15, 0.20, 1.0))
                glLightfv(GL_LIGHT0, GL_AMBIENT, (0.05, 0.05, 0.08, 1.0))

        # =====================================================
        # FLOOR
        # =====================================================
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)

        glBindTexture(GL_TEXTURE_2D, tex.load("floor.jpg"))
        draw_textured_quad(S, S, uv_scale=6.0)

        # =====================================================
        # SUN BRIGHT SPOT (DAY ONLY)
        # =====================================================
        if mode == "day":
            glPushAttrib(GL_ENABLE_BIT | GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glDisable(GL_LIGHTING)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

            glEnable(GL_DEPTH_TEST)
            glDepthMask(GL_FALSE)

            glColor4f(1.0, 0.95, 0.8, 0.35)

            y = 0.02
            z0 = -hs + 0.8
            z1 = -hs + 2.5

            glBegin(GL_QUADS)
            glVertex3f(-1.6, y, z0)
            glVertex3f( 1.6, y, z0)
            glVertex3f( 2.6, y, z1)
            glVertex3f(-2.6, y, z1)
            glEnd()

            glDepthMask(GL_TRUE)
            glDisable(GL_BLEND)
            glPopAttrib()

        # =====================================================
        # RUG
        # =====================================================
        glBindTexture(GL_TEXTURE_2D, tex.load("rug.jpg"))
        glPushMatrix()
        glTranslatef(0.0, 0.01, 0.3)
        draw_textured_quad(3.2, 2.2, uv_scale=1.0)
        glPopMatrix()

        # =====================================================
        # CEILING
        # =====================================================
        glBindTexture(GL_TEXTURE_2D, tex.load("wall.jpg"))
        self._quad(
            (-hs, H, -hs), ( hs, H, -hs),
            ( hs, H,  hs), (-hs, H,  hs),
            (0.0, -1.0, 0.0), uv=(6.0, 6.0)
        )

        # =====================================================
        # BACK WALL (WINDOW HOLE)
        # =====================================================
        self._quad(
            (-hs, 0.0, -hs), (-1.2, 0.0, -hs),
            (-1.2, H, -hs), (-hs, H, -hs),
            (0.0, 0.0, 1.0), uv=(3.0, 3.0)
        )
        self._quad(
            (1.2, 0.0, -hs), (hs, 0.0, -hs),
            (hs, H, -hs), (1.2, H, -hs),
            (0.0, 0.0, 1.0), uv=(3.0, 3.0)
        )
        self._quad(
            (-1.2, 0.0, -hs), (1.2, 0.0, -hs),
            (1.2, 1.1, -hs), (-1.2, 1.1, -hs),
            (0.0, 0.0, 1.0)
        )
        self._quad(
            (-1.2, 2.2, -hs), (1.2, 2.2, -hs),
            (1.2, H, -hs), (-1.2, H, -hs),
            (0.0, 0.0, 1.0)
        )

        # =====================================================
        # FRONT & SIDE WALLS
        # =====================================================
        self._quad(
            ( hs, 0.0,  hs), (-hs, 0.0,  hs),
            (-hs, H,  hs), ( hs, H,  hs),
            (0.0, 0.0, -1.0), uv=(6.0, 3.0)
        )
        self._quad(
            (-hs, 0.0,  hs), (-hs, 0.0, -hs),
            (-hs, H, -hs), (-hs, H,  hs),
            (1.0, 0.0, 0.0), uv=(6.0, 3.0)
        )
        self._quad(
            ( hs, 0.0, -hs), ( hs, 0.0,  hs),
            ( hs, H,  hs), ( hs, H, -hs),
            (-1.0, 0.0, 0.0), uv=(6.0, 3.0)
        )

        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)

        # =====================================================
        # WINDOW GLASS
        # =====================================================
        glPushAttrib(GL_ENABLE_BIT | GL_CURRENT_BIT)

        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        if mode == "day":
            glColor4f(0.6, 0.8, 1.0, 0.75)
        else:
            glColor4f(0.1, 0.12, 0.2, 0.7)

        z = -hs + 0.02
        glBegin(GL_QUADS)
        glVertex3f(-1.2, 1.1, z)
        glVertex3f( 1.2, 1.1, z)
        glVertex3f( 1.2, 2.2, z)
        glVertex3f(-1.2, 2.2, z)
        glEnd()

        glPopAttrib()
