# 🏠 Bedroom Showcase

**A 3D Interactive Bedroom Visualization Engine**

> Explore and interact with a beautifully rendered 3D bedroom environment with realistic lighting, dynamic camera control, and immersive interior design visualization.

---

## ✨ Features

- **3D Room Rendering** - Fully rendered bedroom with multiple furniture pieces
- **Interactive Camera Control** - Navigate through the space freely
- **Dynamic Lighting System** - Realistic light sources and shadow casting
- **Furniture Objects** - Bed, desk, chair, lamp, drawer, and more
- **Texture Mapping** - Detailed surface textures for realism
- **Real-time Performance** - Smooth rendering at interactive frame rates

---

## 🎨 Project Highlights

- Custom 3D geometry primitives (cubes, planes, etc.)
- UV mapping and texture application
- Hierarchical entity system for scene management
- Input-responsive camera navigation
- Time-based animation support

---

## 🛠️ Technology Stack

- **Language:** Python
- **Graphics:** OpenGL (via custom renderer)
- **3D Math:** Custom matrix and vector operations
- **Architecture:** Object-oriented entity-component design

---

## 🚀 Getting Started

### Requirements
```bash
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
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── assets/              # Textures and resources
├── src/
│   ├── app.py          # Main application class
│   ├── renderer.py     # Rendering engine
│   ├── camera.py       # Camera control
│   ├── lighting.py     # Lighting system
│   ├── entities/       # 3D objects (bed, chair, desk, etc.)
│   ├── geometry/       # 3D primitives and UV mapping
│   └── scene/          # Scene management
```

---

## 🎮 Controls

- **Mouse** - Camera look-around
- **WASD** - Movement
- **ESC** - Exit

---

## 📝 License

This project is for educational and portfolio purposes.

---

**Created with ❤️ for 3D graphics enthusiasts**
