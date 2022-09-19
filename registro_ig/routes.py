from registro_ig import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html", pageTitle="Lista", movimientos=[])

@app.route("/alta")
def alta():
    return render_template("new.html", pageTitle="Alta")

@app.route("/baja")
def baja():
    return render_template("baja.html", pageTitle="Baja")

@app.route("/modif")
def modificacion():
    return render_template("modif.html", pageTitle="Modificacion")