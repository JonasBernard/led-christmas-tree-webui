from abc import ABC, abstractmethod

class Effect(ABC):
    def __init__(self, adapter) -> None:
        self.params = {}

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def teardown(self):
        pass

    def set_param(self, key, value):
        self.params[key] = value