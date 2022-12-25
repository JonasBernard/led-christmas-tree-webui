from effects.effect import Effect
import threading
import math
import time
import random


class BreatheEffect(Effect):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)
        self.adapter = adapter
        self.started = False
        self.params = {
            "min": 0.2,
            "max": 0.6,
            "frequency": 2.0
        }

    def setup(self):
        self.runner = threading.Thread(target=self.runner, args=[
                                       self.adapter, lambda: self.started, lambda: self.params["min"], 
                                       lambda: self.params["max"], lambda: self.params["frequency"]])
        self.started = True
        self.runner.start()

    def teardown(self):
        self.started = False
        self.runner.join()

    def runner(self, adapter, should_run_on, min, max, frequency):
        while should_run_on():
            # set the brightness to a value between min and max based on a sine wave with the specified frequency
            brightness = ((math.sin(time.time() * frequency())+1) /
                          2) * (max()-min()) + min()
            adapter.set_brightness(brightness)
