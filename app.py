from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

    casa = [
    {"lugar": "Sala", "ancho": "4.20 m", "largo": "4 m", "altura": "2.22 m"},
    {"lugar": "Cocina", "ancho": "1.90 m", "largo": "3.30 m", "altura": "2.22 m"},
    {"lugar": "Pasillo", "ancho": "4.20 m", "largo": "10.43 m", "altura": "2.22 m"},
    {"lugar": "Habitación 1", "ancho": "2.22 m", "largo": "3 m", "altura": "2.22 m"},
    {"lugar": "Habitación 2", "ancho": "2.33 m", "largo": "3 m", "altura": "2.22 m"},
    {"lugar": "Habitación 3", "ancho": "2.85 m", "largo": "2.73 m", "altura": "2.22 m"},
    {"lugar": "Baño 1", "ancho": "1 m", "largo": "2 m", "altura": "2.22 m"},
    {"lugar": "Baño 2", "ancho": "1.17 m", "largo": "2 m", "altura": "2.22 m"},
    {"lugar": "Balcón", "ancho": "8 m", "largo": "3.70 m", "altura": "2.22 m"}
]

    return render_template("index.html", casa=casa)

if __name__ == "__main__":
    app.run(debug=True)