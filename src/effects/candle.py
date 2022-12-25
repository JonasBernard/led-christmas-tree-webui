from effects.effect import Effect
import threading
import time
import random
from colorzero import Lightness


class CandleEffect(Effect):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)
        self.adapter = adapter
        self.started = False
        self.params = {
            "factor": 0.7,
            "windiness": 0.2
        }

    def setup(self):
        self.thread = threading.Thread(target=self.runner, args=[
            self.adapter,
            lambda: self.started,
            lambda: self.params["factor"],
            lambda: self.adapter.get_color(),
            lambda: self.params["windiness"]
        ])
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()

    def runner(self, adapter, should_run_on, factor, base_color, windiness):
        while should_run_on():
            for pixel in adapter.get_pixels():
                if (random.random() < windiness() and pixel.get_color().difference(base_color()) < 0.05):
                    rand = factor() * random.random()
                    pixel.set_color(base_color() * Lightness(rand))
                else:
                    pixel.set_color(base_color())
