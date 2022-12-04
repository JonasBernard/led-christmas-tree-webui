from abc import ABC, abstractmethod

class Adapter(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def set_color(self, color):
        pass