import time
from OpenGL.GL import *
from OpenGL.GLUT import glutBitmapCharacter, GLUT_BITMAP_HELVETICA_18

class Clock:
    """
    Jam digital sederhana:
    - Menggambar teks jam (HH:MM:SS) di atas meja.
    Catatan: Menggunakan GLUT bitmap font.
    """
    def __init__(self):
        self.visible = True

        # posisi di area meja (sesuaikan dengan Desk.pos)
        self.pos = (2.0, 0.95, -1.0)

    def update(self, dt, ctx):
        pass

    def draw(self, ctx):
        lighting = ctx["lighting"]
        mode = getattr(lighting, "mode", "day")

        # teks harus terlihat jelas: matikan lighting sementara
        glPushAttrib(GL_ENABLE_BIT | GL_CURRENT_BIT)
        glDisable(GL_LIGHTING)
        glDisable(GL_TEXTURE_2D)

        # warna jam: hijau neon malam, gelap sedikit saat siang
        if mode == "night":
            glColor3f(0.2, 1.0, 0.2)
        else:
            glColor3f(0.0, 0.25, 0.0)

        glRasterPos3f(self.pos[0], self.pos[1], self.pos[2])

        t = time.strftime("%H:%M:%S")
        for ch in t:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

        glPopAttrib()
