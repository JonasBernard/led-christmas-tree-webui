from effects.effect import Effect
import threading
import time
import random


class CandleEffect(Effect):
    def __init__(self, adapter) -> None:
        self.adapter = adapter
        self.started = False
        self.min = 0.2
        self.max = 0.6
        self.windiness = 0.3
        self.thread = threading.Thread(target=self.flicker_thread, args=[adapter,
                                                                         lambda: self.started,
                                                                         lambda: self.min,
                                                                         lambda: self.max,
                                                                         self.adapter.get_color(),
                                                                         lambda: self.windiness
                                                                         ])

    def setup(self):
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()

    def flicker_thread(self, adapter, should_run_on, min, max, base_color, windiness):
        while should_run_on():

            for pixel in adapter.get_pixels():
                if (random.random() < windiness()):
                    r,g,b = base_color
                    dark = (r * 0.1, g * 0.1, b * 0.1)
                    pixel.color(dark)
                else:
                    pixel.color(base_color)

            time.sleep(0.1)
