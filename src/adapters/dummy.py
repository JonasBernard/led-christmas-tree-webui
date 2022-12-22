from adapters.adapter import Adapter, PixelAdapter

class DummyAdapter(Adapter):
    def __init__(self) -> None:
        super().__init__()

    def off(self):
        print("Turned tree off")

    def on(self):
        print("Turned tree on")

    def set_color(self, color):
        print("Set color to " + color)

    def set_brightness(self, brightness):
        self.brightness = brightness
        print("Set brightness to " + str(brightness))

    def get_brightness(self):
        return self.brightness

    def tree(self):
        return [DummyPixel(id) for id in range(1, 25)]

class DummyPixel(PixelAdapter):
    def __init__(self, pixel_or_id) -> None:
        super().__init__()
        self.id = pixel_or_id
    
    def set_brightness(self, brightness):
        print("[Pixel " + self.id + "] Set brightness to " + str(brightness))