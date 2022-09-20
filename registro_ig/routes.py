from registro_ig import app
import csv
from flask import render_template, request,redirect
from datetime import date


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
        return render_template("new.html", pageTitle="Alta", 
                               dataForm={})
    else:
        errores = validaFormulario(request.form)

        if not errores:
            fichero = open("data/movimientos.txt", "a", newline="")
            csvWriter = csv.writer(fichero, delimiter=",", quotechar='"')

            csvWriter.writerow([request.form['date'], request.form['concept'], request.form['quantity']])
            fichero.close()

            return redirect("/")
        else:
            return render_template("new.html", pageTitle="Alta", msgErrors=errores, dataForm=dict(request.form))


def validaFormulario(camposFormulario):
    errores = []
    hoy = date.today().isoformat()
    if camposFormulario["date"] > hoy:
        errores.append("La fecha introucida es el futuro")

    if camposFormulario['concept'] == "":
        errores.append("Introduce un concepto para la transacción")
    
    if camposFormulario['quantity'] == "" or float(camposFormulario['quantity']) == 0.0:
        errores.append("Introduce una cantidad positiva o negativa")
    
    return errores

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    return f"Deberia borrar el registro {id}"



