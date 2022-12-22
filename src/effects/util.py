from effects.none import NoneEffect
from effects.candle import CandleEffect

class EffectUtils:
    def get_effect_by_name(name, adapter):
        effect = NoneEffect(adapter)
        if name == "candle":
            effect = CandleEffect(adapter)
        return effect