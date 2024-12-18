#PASO 1: IMPORTAR FLASK
from flask import Flask, render_template, url_for

#PASO 2: CREAR UNA INSTANCIA DE FLASK
app = Flask(__name__)

#PASO 3: RUTAS

#ruta principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/user/<username>')
def user(username):
    return render_template("user.html", username=username)

@app.route('/validate_adult/<int:age>')
def validate_adult(age):
    if age >= 18:
        return 'adult'
    else:
        return 'minor'

#PASO 4: CORRER EL SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)