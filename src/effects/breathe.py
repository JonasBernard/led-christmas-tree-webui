from effects.effect import Effect
import threading
import math
import time
import random

class BreatheEffect(Effect):
    def __init__(self, adapter) -> None:
        self.adapter = adapter
        self.started = False
        self.min = 0.2
        self.max = 0.6
        self.frequency = 2
        self.thread = threading.Thread(target=self.flicker_thread, args=[adapter, lambda: self.started, lambda: self.min, lambda: self.max, lambda: self.frequency])

    def setup(self):
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()

    def flicker_thread(self, adapter, should_run_on, min, max, frequency):
        while should_run_on():
            # set the brightness to a value between min and max based on a sine wave with the specified frequency
            brightness = ((math.sin(time.time() * frequency())+1)/2) * (max()-min()) + min()
            adapter.set_brightness(brightness)