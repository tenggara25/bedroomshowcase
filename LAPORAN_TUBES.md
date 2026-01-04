# LAPORAN TUGAS BESAR
## GRAFIKA KOMPUTER

---

# 🏠 BEDROOM SHOWCASE
### Visualisasi Ruang Kamar Tidur 3D Interaktif

---

## 📋 INFORMASI KELOMPOK

| No | Nama | NIM |
|----|------|-----|
| 1 | Fachri Reyhan | 0112523013 |
| 2 | Alamsyah Hutama | 0112523004 |
| 3 | Ralf Fadila | 0112523048 |
| 4 | Ariq Gymnastiar P. | 0102521704 |

**Mata Kuliah:** Grafika Komputer  
**Dosen Pengampu:** Riri Safitri  
**Tahun Akademik:** 2025/2026

---

## 1. DESKRIPSI PROYEK

### 1.1 Latar Belakang
Proyek "Bedroom Showcase" adalah aplikasi visualisasi 3D interaktif yang menampilkan sebuah kamar tidur lengkap dengan berbagai furnitur dan fitur pencahayaan. Aplikasi ini dibangun menggunakan Python dengan library PyOpenGL untuk merender grafik 3D secara real-time.

### 1.2 Tujuan
- Mengimplementasikan konsep-konsep grafika komputer dalam aplikasi nyata
- Membuat visualisasi 3D interaktif dengan kontrol kamera first-person
- Menerapkan sistem pencahayaan dinamis (day/night mode)
- Mengimplementasikan texture mapping pada objek 3D
- Membuat animasi pada objek-objek dalam scene

### 1.3 Deskripsi Animasi dan Fitur

#### A. Objek 3D dalam Scene
| No | Objek | Deskripsi |
|----|-------|-----------|
| 1 | Room | Ruangan dengan dinding, lantai, langit-langit bertekstur |
| 2 | Bed | Tempat tidur dengan bantal dan selimut |
| 3 | Desk | Meja kerja |
| 4 | Chair | Kursi dengan sandaran |
| 5 | Drawer/Nightstand | Laci/nakas di samping tempat tidur |
| 6 | Lamp | Lampu gantung di langit-langit |
| 7 | Clock | Jam dinding dengan jarum bergerak |
| 8 | Laptop | Laptop di atas meja dengan layar menyala |
| 9 | Bookshelf | Rak buku dengan buku-buku berwarna |
| 10 | Door | Pintu dengan animasi buka/tutup |
| 11 | Desk Lamp | Lampu meja yang bisa dinyalakan/dimatikan |
| 12 | Plant | Tanaman hias dengan animasi bergoyang |
| 13 | Ceiling Fan | Kipas angin langit-langit yang berputar |
| 14 | Wardrobe | Lemari pakaian dengan pintu animasi |
| 15 | Curtain | Gorden jendela |
| 16 | Window/Skybox | Jendela dengan pemandangan langit (matahari/bulan/bintang) |

#### B. Animasi yang Diimplementasikan
1. **Animasi Jam** - Jarum jam bergerak sesuai waktu real-time
2. **Animasi Pintu** - Pintu dapat dibuka/ditutup dengan rotasi smooth
3. **Animasi Kipas** - Kipas angin berputar kontinyu
4. **Animasi Tanaman** - Daun tanaman bergoyang dengan sine wave
5. **Animasi Lemari** - Pintu lemari dapat dibuka/ditutup
6. **Animasi Skybox** - Matahari/bulan bergerak, bintang berkedip
7. **Animasi Kamera** - Auto-tour mode dan smooth transitions

---

## 2. FUNGSI DAN TEKNIK YANG DIGUNAKAN

### 2.1 Transformasi Geometri

#### A. Translasi (Translation)
Digunakan untuk memposisikan objek dalam ruang 3D.

```python
# Contoh translasi untuk memindahkan objek
glTranslatef(x, y, z)

# Implementasi pada bed.py
glPushMatrix()
glTranslatef(self.position[0], self.position[1], self.position[2])
# ... render objek
glPopMatrix()
```

#### B. Rotasi (Rotation)
Digunakan untuk memutar objek pada sumbu tertentu.

```python
# Rotasi pada sumbu Y (yaw)
glRotatef(angle, 0, 1, 0)

# Implementasi pada kipas angin (ceiling_fan.py)
glRotatef(self.rotation, 0, 1, 0)  # Putar bilah kipas

# Implementasi pada pintu (door.py)
glRotatef(self.current_angle, 0, 1, 0)  # Animasi buka pintu
```

#### C. Scaling
Digunakan untuk mengubah ukuran objek.

```python
# Scaling objek
glScalef(sx, sy, sz)

# Implementasi pada primitives.py untuk membuat box
def draw_box(width, height, depth):
    glPushMatrix()
    glScalef(width, height, depth)
    # ... render unit cube
    glPopMatrix()
```

### 2.2 Proyeksi (Projection)

#### A. Proyeksi Perspektif
Digunakan untuk memberikan efek kedalaman yang realistis.

```python
# Setup projection matrix (renderer.py)
def setup_projection(self):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(
        60.0,           # Field of View (FOV)
        self.aspect,    # Aspect Ratio (width/height)
        0.1,            # Near clipping plane
        100.0           # Far clipping plane
    )
    glMatrixMode(GL_MODELVIEW)
```

#### B. View Matrix (Camera)
Implementasi kamera first-person dengan gluLookAt.

```python
# camera.py
def apply(self):
    # Hitung target berdasarkan yaw dan pitch
    target_x = self.position[0] + math.cos(math.radians(self.yaw))
    target_y = self.position[1] + math.sin(math.radians(self.pitch))
    target_z = self.position[2] + math.sin(math.radians(self.yaw))
    
    gluLookAt(
        self.position[0], self.position[1], self.position[2],  # Eye position
        target_x, target_y, target_z,                           # Look at
        0, 1, 0                                                  # Up vector
    )
```

### 2.3 Lighting (Pencahayaan)

#### A. Setup Lighting
Menggunakan model pencahayaan Phong dengan multiple light sources.

```python
# lighting.py
def setup_lighting(self):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Lampu langit-langit
    glEnable(GL_LIGHT1)  # Cahaya jendela
    glEnable(GL_LIGHT2)  # Lampu meja
    
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
```

#### B. Day/Night Mode
Sistem pencahayaan dinamis dengan dua mode.

```python
# lighting.py
def set_day_mode(self):
    # Ambient light tinggi untuk siang
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.4, 0.4, 0.4, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.9, 0.9, 0.85, 1.0])
    
    # Cahaya jendela terang
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 0.95, 0.8, 1.0])

def set_night_mode(self):
    # Ambient light rendah untuk malam
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.1, 0.1, 0.15, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.4, 0.35, 0.3, 1.0])
```

#### C. Point Light dengan Attenuation
Lampu meja dengan efek atenuasi jarak.

```python
# desklamp.py
def update_light(self):
    if self.is_on:
        glEnable(GL_LIGHT2)
        light_pos = [self.position[0], self.position[1] + 0.5, self.position[2], 1.0]
        glLightfv(GL_LIGHT2, GL_POSITION, light_pos)
        glLightfv(GL_LIGHT2, GL_DIFFUSE, [1.0, 0.95, 0.8, 1.0])
        
        # Attenuation - cahaya melemah seiring jarak
        glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 1.0)
        glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.09)
        glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 0.032)
```

### 2.4 Texture Mapping

#### A. Loading Texture
Memuat gambar dan mengkonversi ke texture OpenGL.

```python
# textures.py
def load_texture(filepath):
    image = Image.open(filepath)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = image.convert("RGBA").tobytes()
    
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    
    return texture_id
```

#### B. Applying Texture dengan UV Mapping
Menerapkan texture pada permukaan dengan koordinat UV.

```python
# Contoh texture mapping pada dinding (room.py)
def draw_textured_wall(self):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, self.wall_texture)
    
    glBegin(GL_QUADS)
    # UV coordinates (0,0) sampai (repeat, repeat) untuk tiling
    glTexCoord2f(0, 0); glVertex3f(-4, -1, -4)
    glTexCoord2f(2, 0); glVertex3f(4, -1, -4)
    glTexCoord2f(2, 2); glVertex3f(4, 3, -4)
    glTexCoord2f(0, 2); glVertex3f(-4, 3, -4)
    glEnd()
    
    glDisable(GL_TEXTURE_2D)
```

### 2.5 Animasi

#### A. Time-Based Animation
Animasi berdasarkan waktu untuk konsistensi frame rate.

```python
# time.py
class TimeManager:
    def __init__(self):
        self.last_time = time.time()
        self.delta_time = 0
        
    def update(self):
        current = time.time()
        self.delta_time = current - self.last_time
        self.last_time = current
        return self.delta_time
```

#### B. Animasi Rotasi (Kipas Angin)
```python
# ceiling_fan.py
def update(self, delta_time):
    if self.is_running:
        # Rotasi 180 derajat per detik
        self.rotation += 180 * delta_time
        if self.rotation >= 360:
            self.rotation -= 360
```

#### C. Animasi Sine Wave (Tanaman Bergoyang)
```python
# plant.py
def update(self, delta_time):
    self.time += delta_time
    # Gerakan bergoyang dengan sine wave
    self.sway = math.sin(self.time * 2) * 5  # Amplitude 5 derajat

def render(self):
    glPushMatrix()
    glRotatef(self.sway, 0, 0, 1)  # Goyang pada sumbu Z
    self.draw_leaves()
    glPopMatrix()
```

#### D. Animasi Interpolasi (Smooth Door Opening)
```python
# door.py
def update(self, delta_time):
    # Lerp dari sudut saat ini ke target
    if self.is_open:
        self.target_angle = 90
    else:
        self.target_angle = 0
    
    # Smooth interpolation
    self.current_angle += (self.target_angle - self.current_angle) * 5 * delta_time
```

#### E. Smooth Camera Transitions
```python
# renderer.py
def update_camera_transition(self, delta_time):
    if self.transitioning:
        self.transition_progress += delta_time * 2
        t = min(self.transition_progress, 1.0)
        
        # Linear interpolation
        self.camera.position[0] = self.start_pos[0] + (self.target_pos[0] - self.start_pos[0]) * t
        self.camera.position[1] = self.start_pos[1] + (self.target_pos[1] - self.start_pos[1]) * t
        self.camera.position[2] = self.start_pos[2] + (self.target_pos[2] - self.start_pos[2]) * t
```

### 2.6 Collision Detection

Deteksi tabrakan dengan dinding dan objek menggunakan AABB (Axis-Aligned Bounding Box).

```python
# camera.py
def check_collision(self, new_x, new_z):
    # Batas dinding
    margin = 0.5
    if new_x < -3.5 or new_x > 3.5:
        return True
    if new_z < -3.5 or new_z > 3.5:
        return True
    
    # Bounding box untuk setiap objek
    obstacles = [
        (-3.5, -3.5, -1.5, -1.5),  # Bed
        (2.2, -3.0, 4.2, -1.0),     # Desk
        # ... obstacle lainnya
    ]
    
    for (min_x, min_z, max_x, max_z) in obstacles:
        if min_x <= new_x <= max_x and min_z <= new_z <= max_z:
            return True
    
    return False

def move(self, direction, delta_time):
    new_x = self.position[0] + direction[0] * self.speed * delta_time
    new_z = self.position[2] + direction[2] * self.speed * delta_time
    
    if not self.check_collision(new_x, new_z):
        self.position[0] = new_x
        self.position[2] = new_z
```

### 2.7 Matrix Stack Operations

Menggunakan glPushMatrix/glPopMatrix untuk hierarki transformasi.

```python
# Contoh hierarki pada ceiling fan
def render(self):
    glPushMatrix()
    glTranslatef(0, 2.5, 0)  # Posisi di langit-langit
    
    # Render body kipas
    self.draw_body()
    
    # Render bilah kipas dengan rotasi
    glPushMatrix()
    glRotatef(self.rotation, 0, 1, 0)
    self.draw_blades()
    glPopMatrix()
    
    glPopMatrix()
```

### 2.8 Skybox dengan Day/Night Cycle

```python
# room.py - Skybox implementation
def draw_skybox(self):
    if self.is_day:
        # Gradient langit biru
        glBegin(GL_QUADS)
        glColor3f(0.4, 0.7, 1.0)  # Biru muda atas
        glVertex3f(-10, 5, -15)
        glColor3f(0.7, 0.85, 1.0)  # Lebih terang bawah
        glVertex3f(-10, -1, -15)
        glEnd()
        
        # Gambar matahari
        self.draw_sun()
        self.draw_clouds()
    else:
        # Langit malam gelap
        glColor3f(0.05, 0.05, 0.15)
        # ... render langit malam
        
        # Gambar bulan dan bintang
        self.draw_moon()
        self.draw_stars()
```

---

## 3. SCRIPT / SOURCE CODE

### 3.1 Struktur File

```
bedroomshowcase/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── assets/textures/        # Texture images
└── src/
    ├── app.py             # Main application
    ├── renderer.py        # OpenGL rendering
    ├── camera.py          # First-person camera
    ├── lighting.py        # Lighting system
    ├── config.py          # Configuration
    ├── time.py            # Time management
    ├── input.py           # Input handling
    ├── textures.py        # Texture loading
    ├── math3d.py          # Math utilities
    ├── entities/          # 3D objects
    │   ├── base.py
    │   ├── room.py
    │   ├── bed.py
    │   ├── desk.py
    │   ├── chair.py
    │   ├── drawer.py
    │   ├── lamp.py
    │   ├── clock.py
    │   ├── laptop.py
    │   ├── door.py
    │   ├── bookshelf.py
    │   ├── desklamp.py
    │   ├── plant.py
    │   ├── ceiling_fan.py
    │   ├── wardrobe.py
    │   ├── curtain.py
    │   ├── shadows.py
    │   └── hud.py
    ├── geometry/
    │   └── primitives.py
    └── scene/
        ├── base_scene.py
        └── bedroom_scene.py
```

### 3.2 Main Entry Point (main.py)

```python
from src.app import App

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
```

### 3.3 Application Class (src/app.py)

```python
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.renderer import Renderer
from src.camera import Camera
from src.scene.bedroom_scene import BedroomScene
from src.time import TimeManager
from src.input import InputHandler
from src.config import *

class App:
    def __init__(self):
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.renderer = None
        self.camera = None
        self.scene = None
        self.time_manager = TimeManager()
        self.input_handler = InputHandler()
        
    def init_glut(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow(b"Bedroom Showcase - 3D Interactive Room")
        
    def init_opengl(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)
        glClearColor(0.1, 0.1, 0.15, 1.0)
        
    def setup_callbacks(self):
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.special_keys)
        glutPassiveMotionFunc(self.mouse_motion)
        glutIdleFunc(self.idle)
        
    def run(self):
        self.init_glut()
        self.init_opengl()
        
        self.camera = Camera()
        self.renderer = Renderer(self.camera)
        self.scene = BedroomScene()
        
        self.setup_callbacks()
        glutSetCursor(GLUT_CURSOR_NONE)
        glutMainLoop()
```

*(Source code lengkap terlampir dalam repository)*

---

## 4. OUTPUT / LUARAN

### 4.1 Tampilan Aplikasi

#### Mode Siang (Day Mode)
- Ruangan terang dengan cahaya natural dari jendela
- Langit biru dengan matahari dan awan
- Semua detail furnitur terlihat jelas

#### Mode Malam (Night Mode)
- Pencahayaan redup dari lampu langit-langit
- Langit gelap dengan bulan dan bintang
- Lampu meja dapat dinyalakan untuk pencahayaan tambahan

### 4.2 Fitur Interaktif

| Tombol | Fungsi |
|--------|--------|
| W/A/S/D | Gerak maju/kiri/mundur/kanan |
| Mouse | Melihat sekeliling |
| L | Toggle day/night mode |
| M | Toggle lampu meja |
| F | Toggle kipas angin |
| O | Buka/tutup pintu |
| K | Buka/tutup lemari |
| T | Toggle auto-tour |
| 1-6 | Preset camera views |
| R | Reset posisi kamera |
| ESC | Keluar aplikasi |

### 4.3 Screenshot

*[Lampirkan screenshot aplikasi di sini]*

1. **Overview Room** - Tampilan keseluruhan kamar
2. **Day Mode** - Tampilan mode siang
3. **Night Mode** - Tampilan mode malam
4. **Furniture Details** - Detail furnitur (bed, desk, wardrobe)
5. **Animations** - Kipas berputar, pintu terbuka, tanaman bergoyang

### 4.4 Video Demo

*[Link video demo: _______________]*

---

## 5. KESIMPULAN

### 5.1 Pencapaian
Proyek Bedroom Showcase berhasil mengimplementasikan:

1. **Transformasi Geometri** - Translasi, rotasi, dan scaling untuk memposisikan dan menganimasikan objek
2. **Proyeksi Perspektif** - Menggunakan gluPerspective untuk tampilan 3D realistis
3. **Sistem Pencahayaan** - Multiple light sources dengan day/night mode
4. **Texture Mapping** - Penerapan texture pada dinding, lantai, dan objek
5. **Animasi Real-time** - Berbagai animasi seperti kipas, pintu, tanaman, dan jam
6. **Interaksi User** - Kontrol kamera first-person dan interaksi dengan objek

### 5.2 Pembelajaran
- Pemahaman mendalam tentang pipeline rendering OpenGL
- Implementasi sistem entity-component untuk manajemen scene
- Teknik optimasi rendering untuk performa real-time
- Penggunaan matrix stack untuk hierarki transformasi

### 5.3 Pengembangan Selanjutnya
- Implementasi shadow mapping untuk bayangan realistis
- Penambahan efek post-processing (bloom, ambient occlusion)
- Sistem partikel untuk efek debu, cahaya
- Audio/sound effects

---

## 6. REFERENSI

1. **OpenGL Programming Guide (Red Book)** - Dave Shreiner, Graham Sellers, et al.
   - Referensi utama untuk fungsi-fungsi OpenGL

2. **PyOpenGL Documentation** - http://pyopengl.sourceforge.net/
   - Dokumentasi binding Python untuk OpenGL

3. **Learn OpenGL** - https://learnopengl.com/
   - Tutorial comprehensive untuk konsep grafika komputer modern

4. **OpenGL Transformation** - https://www.songho.ca/opengl/gl_transform.html
   - Penjelasan detail tentang transformasi matrix

5. **OpenGL Lighting** - https://www.khronos.org/opengl/wiki/Lighting
   - Dokumentasi sistem pencahayaan OpenGL

6. **Computer Graphics: Principles and Practice** - John F. Hughes, et al.
   - Buku referensi teori grafika komputer

7. **Python Pillow Documentation** - https://pillow.readthedocs.io/
   - Dokumentasi library untuk loading texture

8. **GLUT Documentation** - https://www.opengl.org/resources/libraries/glut/
   - Referensi untuk windowing dan input handling

---

## LAMPIRAN

### A. Requirements (requirements.txt)
```
PyOpenGL==3.1.7
PyOpenGL-accelerate==3.1.7
Pillow>=10.0.0
```

### B. Cara Menjalankan
```bash
# Clone repository
git clone https://github.com/tenggara25/bedroomshowcase.git
cd bedroomshowcase

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python main.py
```

### C. Repository
**GitHub:** https://github.com/tenggara25/bedroomshowcase

---

*Laporan ini dibuat sebagai dokumentasi Tugas Besar Grafika Komputer*
