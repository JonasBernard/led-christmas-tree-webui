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
        self.effect.teardown()
        self.effect = effect
        self.effect.setup()

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

    @abstractmethod
    def off(self):
        pass
