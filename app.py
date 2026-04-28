from flask import Flask, render_template, request, redirect

app = Flask(__name__)

usuarios = []

@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios)

@app.route('/insertar', methods=['POST'])
def insertar():

    nombre = request.form['nombre']
    correo = request.form['correo']

    usuarios.append({
        'nombre': nombre,
        'correo': correo
    })

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)