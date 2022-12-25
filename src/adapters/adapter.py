from abc import ABC, abstractmethod
from effects.none import NoneEffect

class Adapter(ABC):
    def __init__(self) -> None:
        self.effect = NoneEffect(None)

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def set_brightness(self, brightness):
        pass

    @abstractmethod
    def get_brightness(self):
        pass

    def set_effect(self, effect):
        print("Stopping old effect...")
        self.effect.teardown()
        print("Stopped.")
        self.effect = effect
        print("Start new effect...")
        self.effect.setup()
        print("Started.")

    @abstractmethod
    def get_pixels(self):
        pass

class PixelAdapter(ABC):
    @abstractmethod
    def set_color(self, brightness):
        pass

    @abstractmethod
    def get_color(self):
        pass