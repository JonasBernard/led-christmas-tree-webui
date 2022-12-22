from effects.effect import Effect
import threading
import time
import random
from colorzero import Lightness

class CandleEffect(Effect):
    def __init__(self, adapter) -> None:
        self.adapter = adapter
        self.started = False
        self.factor = 0.7
        self.windiness = 0.2
        self.thread = threading.Thread(target=self.flicker_thread, args=[adapter,
                                                                         lambda: self.started,
                                                                         lambda: self.factor,
                                                                         lambda: self.adapter.get_color(),
                                                                         lambda: self.windiness
                                                                         ])

    def setup(self):
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()

    def flicker_thread(self, adapter, should_run_on, factor, base_color, windiness):
        while should_run_on():
            for pixel in adapter.get_pixels():
                if (random.random() < windiness() and pixel.get_color().difference(base_color()) < 0.05):
                    rand = factor() * random.random()
                    pixel.set_color(base_color() * Lightness(rand))
                else:
                    pixel.set_color(base_color())

