from abc import ABC, abstractmethod

class Effect(ABC):
    def __init__(self, adapter) -> None:
        pass

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def teardown(self):
        pass