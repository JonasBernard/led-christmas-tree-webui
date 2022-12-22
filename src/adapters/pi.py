from adapters.adapter import Adapter
from colorzero import Color
from effects.none import NoneEffect

from lib.tree import RGBXmasTree, Pixel

class PiAdapter(Adapter):
    def __init__(self) -> None:
        super().__init__()
        self.tree = RGBXmasTree()

    def off(self):
        self.effect.teardown()
        self.tree.off()

    def on(self):
        self.tree.on()
        self.effect.setup()

    def set_color(self, color):
        self.tree.color = Color(color)

    def set_brightness(self, brightness):
        self.tree.brightness = brightness

    
