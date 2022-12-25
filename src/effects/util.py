from effects.none import NoneEffect
from effects.candle import CandleEffect
from effects.breathe import BreatheEffect
from effects.party import PartyEffect
from effects.disco import DiscoEffect

class EffectUtils:
    def __init__(self, adapter):
        self.effects = {
            "none": NoneEffect(adapter),
            "breathe": BreatheEffect(adapter),
            "candle": CandleEffect(adapter),
            "party": PartyEffect(adapter),
            "disco": DiscoEffect(adapter),
        } 

    def get_effect_by_name(self, name):
        return self.effects[name]