from registro_ig import app
import csv
from flask import render_template, request,redirect


@app.route("/")
def index():
    fichero = open("data/movimientos.txt", "r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    movimientos = []
    for movimiento in csvReader:
        movimientos.append(movimiento)
    
    fichero.close()
    return render_template("index.html", pageTitle="Lista", movements=movimientos)

@app.route("/alta", methods=["GET","POST"])
def alta():
    if request.method == "GET":
        return render_template("new.html", pageTitle="Alta")
    else:
        fichero = open("data/movimientos.txt", "a", newline="")
        csvWriter = csv.writer(fichero,delimiter=",", quotechar='"')

        csvWriter.writerow([request.form["date"], request.form['concept'], request.form["quantity"]])
        fichero.close()
        return redirect("/")


@app.route("/baja")
def baja():
    return render_template("baja.html", pageTitle="Baja")

@app.route("/modif")
def modificacion():
    return render_template("modif.html", pageTitle="Modificacion")