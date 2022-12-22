from adapters.adapter import Adapter

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
        print("Set brightness to " + str(brightness))
