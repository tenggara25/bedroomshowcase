from OpenGL.GL import *
from src.geometry.primitives import draw_cube
from src.entities.base import Entity

class Bookshelf(Entity):
    def __init__(self):
        super().__init__("Bookshelf")
        self.visible = True
        
        # Posisi di dinding belakang (z = -hs + offset)
        self.pos = (1.0, 0.0, -3.85)
        
        self.width = 1.0
        self.height = 1.6
        self.depth = 0.3
        self.shelf_count = 3

    def update(self, dt, ctx):
        pass

    def _draw_book(self, x, y, z, w, h, d, color):
        glColor3f(*color)
        glPushMatrix()
        glTranslatef(x, y, z)
        glScalef(w, h, d)
        draw_cube(1, 1, 1)
        glPopMatrix()

    def draw(self, ctx):
        tex = ctx["textures"]
        glEnable(GL_TEXTURE_2D)
        glColor3f(1.0, 1.0, 1.0)
        
        glBindTexture(GL_TEXTURE_2D, tex.load("wood.jpg"))

        # Back panel
        glColor3f(0.6, 0.45, 0.35)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + self.height/2, self.pos[2])
        glScalef(self.width, self.height, 0.02)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Left side
        glColor3f(0.55, 0.4, 0.3)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + self.height/2, self.pos[2] + self.depth/2)
        glScalef(0.03, self.height, self.depth)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Right side
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + self.height/2, self.pos[2] - self.depth/2 + self.depth)
        glRotatef(90, 0, 1, 0)
        glTranslatef(0, 0, -self.width/2 + 0.015)
        glScalef(self.depth, self.height, 0.03)
        draw_cube(1, 1, 1)
        glPopMatrix()
        
        # Right side (actual)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1] + self.height/2, self.pos[2] + self.depth - self.depth/2)
        glScalef(0.03, self.height, self.depth)
        draw_cube(1, 1, 1)
        glPopMatrix()

        # Shelves
        shelf_spacing = self.height / (self.shelf_count + 1)
        for i in range(self.shelf_count + 1):
            y = self.pos[1] + i * shelf_spacing
            glColor3f(0.55, 0.4, 0.3)
            glPushMatrix()
            glTranslatef(self.pos[0], y + 0.01, self.pos[2] + self.depth/2)
            glScalef(self.width, 0.02, self.depth)
            draw_cube(1, 1, 1)
            glPopMatrix()

        glBindTexture(GL_TEXTURE_2D, 0)
        
        # Buku-buku dengan berbagai warna
        book_colors = [
            (0.7, 0.2, 0.2),   # merah
            (0.2, 0.5, 0.7),   # biru
            (0.2, 0.6, 0.3),   # hijau
            (0.8, 0.7, 0.2),   # kuning
            (0.6, 0.3, 0.6),   # ungu
            (0.9, 0.5, 0.2),   # orange
            (0.4, 0.3, 0.2),   # coklat
            (0.3, 0.3, 0.5),   # biru gelap
        ]
        
        # Tambah buku di setiap rak
        for shelf in range(self.shelf_count):
            shelf_y = self.pos[1] + (shelf + 1) * shelf_spacing + 0.12
            
            # Buku-buku berdiri
            num_books = 4 + (shelf % 3)  # variasi jumlah buku
            book_x_start = self.pos[0] - 0.01
            
            for b in range(num_books):
                book_w = 0.03 + (b % 3) * 0.01
                book_h = 0.18 + (b % 4) * 0.03
                book_d = 0.12 + (b % 2) * 0.03
                
                color = book_colors[(shelf * 3 + b) % len(book_colors)]
                
                book_z = self.pos[2] + 0.08 + b * 0.06
                
                if book_z < self.pos[2] + self.depth - 0.05:
                    self._draw_book(
                        book_x_start, shelf_y, book_z,
                        book_w, book_h, book_d, color
                    )

        glColor3f(1.0, 1.0, 1.0)
        glDisable(GL_TEXTURE_2D)
