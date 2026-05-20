from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/entrar', methods=['POST'])
def entrar():
    fecha = request.form['fecha']

    if(fecha == '15/3/2024'):
        return render_template('carta.html')
    else:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)