import threading
from effects.effect import Effect
from colorzero import Color

class SpiralEffect(Effect):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)
        self.adapter = adapter
        self.started = False
        self.params = {
            "length": 5,
        }

    def setup(self):
        self.adapter.off()
        self.thread = threading.Thread(target=self.runner, args=[
            self.adapter,
            lambda: self.started,
            lambda: self.params["length"],
        ])
        self.started = True
        self.thread.start()

    def teardown(self):
        self.started = False
        self.thread.join()
        self.adapter.off()

    def runner(self, adapter, should_run_on, length):
        spiral_pixelIndices = [0,16,15,6,12,24,19,7,1,17,14,5,11,23,20,8,2,18,13,4,10,22,21,9,3]
        pixels = adapter.get_pixels()

        try:
            while True:
                trail = [Color(h=j/length(), s=1, v=1) for j in range(length())]
                
                for index in range(len(spiral_pixelIndices)):
                    for i,k in enumerate(trail):
                        pixel = pixels[spiral_pixelIndices[(index-i) % 25]]
                        pixel.set_color(k)

                        if not should_run_on():
                            raise StopIteration
                    pixels[spiral_pixelIndices[(index-len(trail)) % 25]].off()
        except StopIteration:
            pass
