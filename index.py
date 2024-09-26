from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/sobremi')
def sobremi():
    return render_template("sobremi.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/volver')
def volver():
    return render_template("index.html")

@app.route ('/mensaje',methods=['POST'])
def mensaje():
    if request.method == 'POST':
        nom = request == ['nombre']
        mai = request == ['correo']
        
    return render_template('mensaje.html', nombre = nom, correo = mai,)
    


if __name__ == '__main__':
    app.run()
