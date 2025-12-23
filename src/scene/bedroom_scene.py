from src.scene.base_scene import BaseScene
from src.entities.room import Room
from src.entities.bed import Bed
from src.entities.desk import Desk
from src.entities.chair import Chair
from src.entities.drawer import Drawer
from src.entities.lamp import Lamp
from src.entities.clock import Clock
from src.entities.hud import HUD

class BedroomScene(BaseScene):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.room = self.add(Room())
        self.bed = self.add(Bed())
        self.desk = self.add(Desk())
        self.chair = self.add(Chair())
        self.drawer = self.add(Drawer())
        self.lamp = self.add(Lamp())
        self.clock = self.add(Clock())
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
        elif key == b'1': r.set_focus((-2,0.8,1.6),"BED")
        elif key == b'2': r.set_focus((2,0.8,-1.2),"DESK")
        elif key == b'3': r.set_focus((2.6,0.8,-2.6),"DRAWER")
        elif key == b'0': r.clear_focus()
