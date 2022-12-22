from adapters.adapter import Adapter, PixelAdapter
from colorzero import Color

from lib.tree import RGBXmasTree

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
        self.overall_color = color
        self.tree.color = Color(color)

    def get_color(self):
        return self.overall_color

    def set_brightness(self, brightness):
        self.tree.brightness = brightness

    def get_brightness(self):
        return self.tree.brightness

    def get_pixels(self):
        return [PiPixel(pixel) for pixel in self.tree]

class PiPixel(PixelAdapter):
    def __init__(self, pixel_or_id) -> None:
        super().__init__()
        self.pixel = pixel_or_id
    
    def set_color(self, color):
        self.pixel.value = color
