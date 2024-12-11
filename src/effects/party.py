from effects.effect import Effect
import threading
import time
import random
from colorzero import Color

class PartyEffect(Effect):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)
        self.adapter = adapter
        self.started = False
        self.params = {
            "speed": 1,
            "saturation": 1,
            "value": 1,
            "per-pixel": False,
        }

    def setup(self):
        self.thread = threading.Thread(target=self.runner, args=[
            self.adapter,
            lambda: self.started,
            lambda: self.params["speed"],
            lambda: self.params["saturation"],
            lambda: self.params["value"],
            lambda: self.params["per-pixel"]
        ])
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()
        self.adapter.off()

    def runner(self, adapter, should_run_on, speed, saturation, value, per_pixel):
        try:
            while True:
                if not should_run_on():
                    raise StopIteration
                
                if per_pixel():
                    for pixel in adapter.get_pixels():
                        hue = random.random()
                        color = Color(h=hue, s=saturation(), v=value())
                        pixel.set_color(color)

                        if not should_run_on():
                            raise StopIteration
                else:
                    hue = random.random()
                    color = Color(h=hue, s=saturation(), v=value())
                    adapter.set_color(color)
                time.sleep(5 - speed())
        except StopIteration:
            pass