from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/segundapagina">DAR CLIC AQUÍ</a>'


@app.route("/segundapagina")
def bienvenidos():
    return '''
<form method="post" action="/formulario" ">
        <label for="">Nombre</label>
        <input name="mensajero" type="text" placeholder="Ingresa nombre">
        <button type="submit">ENVIAR</button>


'''
@app.route("/formulario", methods= ["post"] )
def elgranform():
    x = request.form.get('mensajero')
    return f'<h1>Hola,bienvenido,{x}. <a href ="/tercerapagina">ENTRA AQUÍ.</a></h1>'

@app.route("/tercerapagina")
def Mi_canal():
    return '<a href="https://www.youtube.com/channel/UCDzUpBTgU2_NJFrrC_w_0Ng">Si quieres, visita mi canal.</a>'


app.run(debug=True)
