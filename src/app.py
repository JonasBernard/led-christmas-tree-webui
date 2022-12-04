from flask import Flask, render_template, url_for, request
from pltfrm import get_adapter

app = Flask(__name__)

adapter = get_adapter()


@app.route("/", methods=['GET'])
def index():
    url_for('static', filename='main.js')
    return render_template("index.html")

@app.post("/tree/on/")
def tree_on():
    adapter.on()
    return { "message": "Turned on" }

@app.post("/tree/off/")
def tree_off():
    adapter.off()
    return { "message": "Turned off" }

@app.post("/tree/color/")
def tree_color_post():
    try:
        color = request.json['color']
    except KeyError as e:
        color = "#ffffff"
    adapter.set_color(color)
    return { "message": "Set color to " + color }
