# 🏠 Bedroom Showcase

**A 3D Interactive Bedroom Visualization Engine**

> Explore and interact with a beautifully rendered 3D bedroom environment with realistic lighting, dynamic camera control, and immersive interior design visualization.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenGL](https://img.shields.io/badge/OpenGL-3.1-green)
![License](https://img.shields.io/badge/License-Educational-orange)

---

## ✨ Features

### 🏠 Room & Environment
- **3D Room Rendering** - Fully rendered bedroom with textured walls, floor, and ceiling
- **Skybox System** - Dynamic day/night cycle with sun, moon, stars, and clouds
- **Window with Curtains** - Realistic window frame with fabric curtains

### 🪑 Furniture & Objects
- **Bed** - Complete with pillows and blanket
- **Desk & Chair** - Work area setup
- **Wardrobe** - With animated opening/closing doors
- **Bookshelf** - Filled with colorful books
- **Nightstand/Drawer** - Bedside storage
- **Laptop** - On desk with glowing screen
- **Plant** - Decorative plant with swaying animation
- **Door** - Animated room entrance

### 💡 Lighting System
- **Day/Night Modes** - Toggle between bright day and cozy night
- **Ceiling Light** - Main room illumination
- **Desk Lamp** - Toggleable point light with attenuation
- **Ceiling Fan** - Rotating fan with light

### 🎥 Camera & Controls
- **First-Person Camera** - Free navigation with mouse look
- **Collision Detection** - Walls and furniture boundaries
- **Auto-Tour Mode** - Automated camera tour of the room
- **Smooth Transitions** - Interpolated camera movements
- **Preset Views** - Quick focus on specific objects

### 📊 HUD & Info
- **FPS Counter** - Real-time performance display
- **Controls Guide** - On-screen keyboard shortcuts
- **Day/Night Indicator** - Current lighting mode

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.12 |
| **Graphics** | PyOpenGL 3.1.7 + GLUT |
| **Textures** | Pillow (PIL) |
| **Architecture** | Entity-Component Pattern |
| **Rendering** | Fixed-function OpenGL Pipeline |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- OpenGL compatible graphics

### Installation
```bash
# Clone the repository
git clone https://github.com/tenggara25/bedroomshowcase.git
cd bedroomshowcase

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
python main.py
```

---

## 📁 Project Structure

```
bedroomshowcase/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── assets/
│   └── textures/          # Texture images
└── src/
    ├── app.py             # Main application & GLUT callbacks
    ├── renderer.py        # OpenGL rendering engine
    ├── camera.py          # First-person camera with collision
    ├── lighting.py        # Multi-light system
    ├── config.py          # Configuration constants
    ├── time.py            # Time & FPS tracking
    ├── input.py           # Input handling
    ├── textures.py        # Texture loading
    ├── math3d.py          # Vector/matrix operations
    ├── entities/
    │   ├── base.py        # BaseEntity class
    │   ├── room.py        # Room with skybox
    │   ├── bed.py         # Bed with pillows
    │   ├── desk.py        # Work desk
    │   ├── chair.py       # Desk chair
    │   ├── drawer.py      # Nightstand
    │   ├── lamp.py        # Ceiling lamp
    │   ├── clock.py       # Wall clock
    │   ├── laptop.py      # Laptop computer
    │   ├── door.py        # Animated door
    │   ├── bookshelf.py   # Bookshelf with books
    │   ├── desklamp.py    # Toggleable desk lamp
    │   ├── plant.py       # Animated plant
    │   ├── ceiling_fan.py # Rotating ceiling fan
    │   ├── wardrobe.py    # Wardrobe with doors
    │   ├── curtain.py     # Window curtains
    │   ├── shadows.py     # Fake shadows
    │   └── hud.py         # HUD overlay
    ├── geometry/
    │   └── primitives.py  # 3D shape generators
    └── scene/
        ├── base_scene.py      # Base scene class
        └── bedroom_scene.py   # Main bedroom scene
```

---

## 🎮 Controls

### Movement
| Key | Action |
|-----|--------|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Strafe left |
| `D` | Strafe right |
| `Mouse` | Look around |

### Interactions
| Key | Action |
|-----|--------|
| `L` | Toggle day/night mode |
| `M` | Toggle desk lamp |
| `F` | Toggle ceiling fan |
| `O` | Open/close door |
| `K` | Open/close wardrobe |
| `T` | Toggle auto-tour |

### Camera Views
| Key | View |
|-----|------|
| `1` | Overview (default) |
| `2` | Focus on bed |
| `3` | Focus on desk |
| `4` | Focus on door |
| `5` | Focus on wardrobe |
| `6` | Focus on plant |

### System
| Key | Action |
|-----|--------|
| `R` | Reset camera position |
| `ESC` | Exit application |

---

## 🖼️ Screenshots

*Coming soon...*

---

## 📝 License

This project is for educational and portfolio purposes.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Created with ❤️ for 3D graphics enthusiasts**
