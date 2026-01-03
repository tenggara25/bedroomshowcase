from OpenGL.GL import *
from OpenGL.GLUT import glutBitmapCharacter, GLUT_BITMAP_8_BY_13
from src.entities.base import Entity

class HUD(Entity):
    def __init__(self):
        super().__init__("HUD")
        self.visible = True
        self.fps = 0.0

    def toggle(self):
        self.visible = not self.visible

    def set_fps(self, fps):
        self.fps = fps

    def update(self, dt, ctx):
        pass

    # ✅ Tambahkan ini agar BaseScene.draw() tidak error
    def draw(self, ctx):
        # HUD tidak digambar di pass 3D
        pass

    def draw_2d(self, ctx, w, h):
        if not self.visible:
            return

        lighting = ctx["lighting"]
        renderer = ctx["renderer"]

        mode = lighting.mode.upper()
        auto = "ON" if renderer.auto_tour else "OFF"
        focus = renderer.focus_name if renderer.focus_name else "-"

        lines = [
            "3D Bedroom Showcase",
            f"FPS: {self.fps:.1f} | Mode: {mode} | AutoTour: {auto}",
            f"Focus: {focus}",
            "",
            "[VIEW]",
            "H: Toggle HUD    T: Auto Tour",
            "N: Day/Night     L: Lighting",
            "",
            "[FOCUS] 1:Bed 2:Desk 3:Nightstand",
            "        4:Bookshelf 5:Wardrobe 6:Plant",
            "        0:Clear Focus",
            "",
            "[INTERACT]",
            "O: Drawer    P: Door    K: Wardrobe",
            "M: Desk Lamp F: Ceiling Fan",
            "",
            "[MOVE] WASD (AutoTour OFF)",
            "ESC: Exit",
        ]

        glPushAttrib(GL_ENABLE_BIT | GL_CURRENT_BIT)
        glDisable(GL_LIGHTING)
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)

        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, w, 0, h, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glColor4f(0, 0, 0, 0.7)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        x, y = 10, h - 280
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x+320, y)
        glVertex2f(x+320, y+270)
        glVertex2f(x, y+270)
        glEnd()

        glColor3f(1, 1, 1)
        ty = y + 252
        for i, line in enumerate(lines):
            glRasterPos2f(x+10, ty - i*14)
            for ch in line:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(ch))

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

        glPopAttrib()
