from effects.effect import Effect
import threading
import math
import time
import random

class CandleEffect(Effect):
    def __init__(self, adapter) -> None:
        self.adapter = adapter
        self.started = False
        self.min = 0.2
        self.max = 0.6
        self.thread = threading.Thread(target=self.flicker_thread, args=[adapter, lambda: self.started, lambda: self.min, lambda: self.max])

    def setup(self):
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()

    def flicker_thread(self, adapter, should_run_on, min, max):
        i = 1
        m = 1
        frequency = 2
        while should_run_on():
            #i = i+1

            #if i % m == 0:
                # set the frequency of the sine wave to a random value between 0.5 and 2 cycles per second
                #frequency = random.uniform(0.5, 2)
                # i = 0
                #m = random.randint(1,5)

            # set the brightness to a value between 0 and 1 based on a sine wave with the specified frequency
            brightness = ((math.sin(time.time() * frequency)+1)/2) * (max()-min()) + min()
            print(brightness)
            adapter.set_brightness(brightness)
            # pause for a short amount of time
            # time.sleep(0.1)
