from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
with open("../models/logistic_default.sav", 'rb') as f:
    model = load(f)

@app.route("/", methods = ["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Tengo que coger los datos que el usuario ha introducido ANTES de pulsar al botón de Predecir
        Pclass = float(request.form["val1"])
        Fare = float(request.form["val2"])
        Sex_n = float(request.form["val3"])
        Embarked_n = float(request.form["val4"])
        FamMembers = float(request.form["val5"])

        data_a_predecir = [[Pclass, Fare, Sex_n, Embarked_n, FamMembers]]
        prediction = model.predict(data_a_predecir)

    return render_template("index.html", prediction = prediction)