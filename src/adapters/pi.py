from adapters.adapter import Adapter
from colorzero import Color

from lib.tree import RGBXmasTree, Pixel

class PiAdapter(Adapter):
    def __init__(self) -> None:
        super().__init__()
        self.tree = RGBXmasTree()

    def off(self):
        self.tree.off()

    def on(self):
        self.tree.on()

    def set_color(self, color):
        self.tree.color = Color(color)