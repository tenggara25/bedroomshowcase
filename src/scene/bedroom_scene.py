from src.scene.base_scene import BaseScene
from src.entities.room import Room
from src.entities.bed import Bed
from src.entities.desk import Desk
from src.entities.chair import Chair
from src.entities.drawer import Drawer
from src.entities.lamp import Lamp
from src.entities.clock import Clock
from src.entities.hud import HUD
from src.entities.laptop import Laptop
from src.entities.door import Door
from src.entities.bookshelf import Bookshelf
from src.entities.desklamp import DeskLamp
from src.entities.plant import Plant
from src.entities.ceiling_fan import CeilingFan
from src.entities.wardrobe import Wardrobe
from src.entities.curtain import Curtain
from src.entities.shadows import Shadows

class BedroomScene(BaseScene):
    def __init__(self, ctx):
        super().__init__(ctx)
        # Shadows first (render di bawah)
        self.shadows = self.add(Shadows())
        self.room = self.add(Room())
        self.bed = self.add(Bed())
        self.desk = self.add(Desk())
        self.chair = self.add(Chair())
        self.drawer = self.add(Drawer())
        self.lamp = self.add(Lamp())
        self.clock = self.add(Clock())
        self.laptop = self.add(Laptop())
        self.door = self.add(Door())
        self.bookshelf = self.add(Bookshelf())
        # New entities
        self.desk_lamp = self.add(DeskLamp())
        self.plant = self.add(Plant())
        self.ceiling_fan = self.add(CeilingFan())
        self.wardrobe = self.add(Wardrobe())
        self.curtain = self.add(Curtain())
        # HUD last
        self.hud = self.add(HUD())

    def on_key(self, key, is_down):
        if not is_down:
            return

        r = self.ctx["renderer"]
        l = self.ctx["lighting"]

        if key in (b'h',b'H'): self.hud.toggle()
        elif key in (b'n',b'N'): l.toggle_mode()
        elif key in (b'l',b'L'): l.enabled = not l.enabled
        elif key in (b't',b'T'): r.auto_tour = not r.auto_tour
        elif key in (b'o',b'O'): self.drawer.toggle()
        elif key in (b'p',b'P'): self.door.toggle()
        elif key in (b'm',b'M'): self.desk_lamp.toggle()
        elif key in (b'f',b'F'): self.ceiling_fan.toggle()
        elif key in (b'k',b'K'): self.wardrobe.toggle()
        elif key == b'1': r.set_focus((-2.5, 0.8, -2.5), "BED")
        elif key == b'2': r.set_focus((3.2, 0.8, -2.0), "DESK")
        elif key == b'3': r.set_focus((-1.2, 0.5, -2.5), "NIGHTSTAND")
        elif key == b'4': r.set_focus((1.0, 1.0, -3.85), "BOOKSHELF")
        elif key == b'5': r.set_focus((-3.5, 1.2, 1.5), "WARDROBE")
        elif key == b'6': r.set_focus((3.2, 0.5, 2.8), "PLANT")
        elif key == b'0': r.clear_focus()
