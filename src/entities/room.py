from OpenGL.GL import *
from src.geometry.primitives import draw_textured_quad
from src.entities.base import Entity

class Room(Entity):
    def __init__(self):
        super().__init__("Room")
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

        # Rug (karpet) di tengah kamar
        glBindTexture(GL_TEXTURE_2D, tex.load("rug.jpg"))
        glPushMatrix()
        glTranslatef(0.0, 0.01, 0.0)  # tengah kamar
        draw_textured_quad(2.5, 2.0, uv_scale=1.0)
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

        # --- Window with skybox effect ---
        glPushAttrib(GL_ENABLE_BIT | GL_CURRENT_BIT)
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        z = -hs + 0.02
        
        if mode == "day":
            # Sky gradient (biru langit)
            glBegin(GL_QUADS)
            # Top - darker blue
            glColor4f(0.4, 0.6, 0.95, 0.9)
            glVertex3f(-1.2, 2.2, z)
            glVertex3f( 1.2, 2.2, z)
            # Bottom - lighter blue
            glColor4f(0.7, 0.85, 1.0, 0.9)
            glVertex3f( 1.2, 1.1, z)
            glVertex3f(-1.2, 1.1, z)
            glEnd()
            
            # Sun
            glColor4f(1.0, 0.95, 0.7, 0.9)
            sun_x, sun_y = 0.6, 1.9
            sun_size = 0.15
            glBegin(GL_QUADS)
            glVertex3f(sun_x - sun_size, sun_y - sun_size, z - 0.01)
            glVertex3f(sun_x + sun_size, sun_y - sun_size, z - 0.01)
            glVertex3f(sun_x + sun_size, sun_y + sun_size, z - 0.01)
            glVertex3f(sun_x - sun_size, sun_y + sun_size, z - 0.01)
            glEnd()
            
            # Clouds
            glColor4f(1.0, 1.0, 1.0, 0.7)
            clouds = [(-0.6, 1.85, 0.3, 0.08), (0.1, 1.95, 0.25, 0.06), (-0.3, 1.75, 0.2, 0.05)]
            for cx, cy, cw, ch in clouds:
                glBegin(GL_QUADS)
                glVertex3f(cx - cw, cy - ch, z - 0.01)
                glVertex3f(cx + cw, cy - ch, z - 0.01)
                glVertex3f(cx + cw, cy + ch, z - 0.01)
                glVertex3f(cx - cw, cy + ch, z - 0.01)
                glEnd()
        else:
            # Night sky gradient
            glBegin(GL_QUADS)
            # Top - dark blue
            glColor4f(0.05, 0.05, 0.15, 0.95)
            glVertex3f(-1.2, 2.2, z)
            glVertex3f( 1.2, 2.2, z)
            # Bottom - slightly lighter
            glColor4f(0.1, 0.1, 0.2, 0.95)
            glVertex3f( 1.2, 1.1, z)
            glVertex3f(-1.2, 1.1, z)
            glEnd()
            
            # Moon
            glColor4f(0.95, 0.95, 0.85, 0.9)
            moon_x, moon_y = -0.5, 1.9
            moon_size = 0.12
            glBegin(GL_QUADS)
            glVertex3f(moon_x - moon_size, moon_y - moon_size, z - 0.01)
            glVertex3f(moon_x + moon_size, moon_y - moon_size, z - 0.01)
            glVertex3f(moon_x + moon_size, moon_y + moon_size, z - 0.01)
            glVertex3f(moon_x - moon_size, moon_y + moon_size, z - 0.01)
            glEnd()
            
            # Stars
            glColor4f(1.0, 1.0, 0.9, 0.8)
            stars = [(0.3, 1.85), (0.7, 1.6), (-0.8, 1.7), (0.5, 2.0), (-0.2, 1.5), 
                     (0.9, 1.85), (-0.9, 1.95), (0.0, 1.8), (0.4, 1.4)]
            for sx, sy in stars:
                star_size = 0.02
                glBegin(GL_QUADS)
                glVertex3f(sx - star_size, sy - star_size, z - 0.01)
                glVertex3f(sx + star_size, sy - star_size, z - 0.01)
                glVertex3f(sx + star_size, sy + star_size, z - 0.01)
                glVertex3f(sx - star_size, sy + star_size, z - 0.01)
                glEnd()

        # Window frame
        glColor4f(0.3, 0.25, 0.2, 1.0)
        frame_thick = 0.05
        # Top frame
        glBegin(GL_QUADS)
        glVertex3f(-1.25, 2.2, z + 0.01)
        glVertex3f( 1.25, 2.2, z + 0.01)
        glVertex3f( 1.25, 2.25, z + 0.01)
        glVertex3f(-1.25, 2.25, z + 0.01)
        glEnd()
        # Bottom frame
        glBegin(GL_QUADS)
        glVertex3f(-1.25, 1.05, z + 0.01)
        glVertex3f( 1.25, 1.05, z + 0.01)
        glVertex3f( 1.25, 1.1, z + 0.01)
        glVertex3f(-1.25, 1.1, z + 0.01)
        glEnd()
        # Left frame
        glBegin(GL_QUADS)
        glVertex3f(-1.25, 1.05, z + 0.01)
        glVertex3f(-1.2, 1.05, z + 0.01)
        glVertex3f(-1.2, 2.25, z + 0.01)
        glVertex3f(-1.25, 2.25, z + 0.01)
        glEnd()
        # Right frame
        glBegin(GL_QUADS)
        glVertex3f(1.2, 1.05, z + 0.01)
        glVertex3f(1.25, 1.05, z + 0.01)
        glVertex3f(1.25, 2.25, z + 0.01)
        glVertex3f(1.2, 2.25, z + 0.01)
        glEnd()
        # Middle divider (vertical)
        glBegin(GL_QUADS)
        glVertex3f(-0.025, 1.1, z + 0.01)
        glVertex3f( 0.025, 1.1, z + 0.01)
        glVertex3f( 0.025, 2.2, z + 0.01)
        glVertex3f(-0.025, 2.2, z + 0.01)
        glEnd()
        # Middle divider (horizontal)
        glBegin(GL_QUADS)
        glVertex3f(-1.2, 1.63, z + 0.01)
        glVertex3f( 1.2, 1.63, z + 0.01)
        glVertex3f( 1.2, 1.68, z + 0.01)
        glVertex3f(-1.2, 1.68, z + 0.01)
        glEnd()

        glPopAttrib()
