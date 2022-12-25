from effects.none import NoneEffect
from effects.candle import CandleEffect
from effects.breathe import BreatheEffect
from effects.party import PartyEffect

class EffectUtils:
    def get_effect_by_name(name, adapter):
        effect = NoneEffect(adapter)
        if name == "breathe":
            effect = BreatheEffect(adapter)
        elif name == "candle":
            effect = CandleEffect(adapter)
        elif name == "party":
            effect = PartyEffect(adapter)
        return effect