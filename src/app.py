from flask import Flask, render_template, url_for, request
from pltfrm import get_adapter
from effects.util import EffectUtils

app = Flask(__name__)

adapter = get_adapter()
effect_utils = EffectUtils(adapter)


@app.route("/", methods=['GET'])
def index():
    url_for('static', filename='main.js')
    return render_template("index.html")

@app.post("/tree/on/")
def tree_on():
    adapter.on()
    return { "message": "Turned tree on." }

@app.post("/tree/off/")
def tree_off():
    adapter.off()
    return { "message": "Turned tree off." }

@app.post("/tree/color/")
def tree_color_post():
    try:
        color = request.json['color']
    except KeyError as e:
        color = "#ffffff"
    adapter.set_color(color)
    return { "message": "Set color to " + color + "."}

@app.post("/tree/brightness/")
def tree_brightness_post():
    try:
        brightness = float(request.json['brightness'])
    except KeyError or Exception as e:
        brightness = 0.5
    adapter.set_brightness(brightness)
    return { "message": "Set brightness to " + str(brightness) + "." }


@app.post("/tree/effect/")
def tree_effect_post():
    try:
        effect_name = request.json['effect-name']
    except KeyError or Exception as e:
        effect_name = "none"
    
    effect = effect_utils.get_effect_by_name(effect_name)
    adapter.set_effect(effect)

    return { "message": "Set effect to " + effect_name + "." }


@app.post("/tree/effect/parameter/")
def tree_effect_param_post():
    try:
        param_key = request.json['key']
        param_value_raw = request.json['value']
        type = request.json['type']
    except KeyError or Exception as e:
        return { "message": "Incomplete request to set effect paramter." }

    param_value = None
    if type == "float":
        param_value = float(param_value_raw)
    if type == "bool":
        param_value = bool(param_value_raw)
    if type == "int":
        param_value = int(param_value_raw)

    if param_value is None:
        return { "message": "Got a parameter of an invalid type." }

    adapter.effect.set_param(param_key, param_value)
    
    return { "message": "Set parameter " + param_key + " to " + str(param_value_raw) }
    