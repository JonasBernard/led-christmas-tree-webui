import threading
import time
from effects.effect import Effect
from colorzero import Color

class HueRotateEffect(Effect):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)
        self.adapter = adapter
        self.started = False
        self.params = {
            "speed": 1,
        }

    def setup(self):
        self.adapter.off()
        self.thread = threading.Thread(target=self.runner, args=[
            self.adapter,
            lambda: self.started,
            lambda: self.params["speed"],
        ])
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()

    def runner(self, adapter, should_run_on, speed):
        steps = 250

        try:
            while True:
                colors = [Color(h=i/steps, s=1, v=1) for i in range(steps)]
                for c in colors:
                    adapter.set_color(c)
                    time.sleep(5 - speed())
                    if not should_run_on():
                        raise StopIteration
        except StopIteration:
            pass

