from effects.effect import Effect

class NoneEffect(Effect):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)

    def setup(self):
        pass

    def teardown(self):
        pass

    def __str__(self) -> str:
        return "no effect"