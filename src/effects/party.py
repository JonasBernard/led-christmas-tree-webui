from effects.effect import Effect
import threading
import time
import random
from colorzero import Color

class PartyEffect(Effect):
    def __init__(self, adapter) -> None:
        self.adapter = adapter
        self.started = False
        self.speed = 1
        self.saturation = 1
        self.value = 1
        self.thread = threading.Thread(target=self.thread, args=[adapter,
                                                                         lambda: self.started,
                                                                         lambda: self.speed,
                                                                         lambda: self.saturation,
                                                                         lambda: self.value
                                                                         ])

    def setup(self):
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()

    def thread(self, adapter, should_run_on, speed, saturation, value):
        while should_run_on():
            hue = random.random()
            color = Color(h=hue, s=saturation(), v=value())
            adapter.set_color(color)
            time.sleep(speed())
