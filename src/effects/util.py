from effects.none import NoneEffect
from effects.candle import CandleEffect
from effects.breathe import BreatheEffect
from effects.party import PartyEffect
from effects.spiral import SpiralEffect
from effects.huerotate import HueRotateEffect

class EffectUtils:
    def __init__(self, adapter):
        self.effects = {
            "none": NoneEffect(adapter),
            "breathe": BreatheEffect(adapter),
            "candle": CandleEffect(adapter),
            "party": PartyEffect(adapter),
            "spiral": SpiralEffect(adapter),
            "huerotate": HueRotateEffect(adapter)
        } 

    def get_effect_by_name(self, name):
        return self.effects[name]
