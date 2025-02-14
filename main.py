from flask import Flask, render_template,request

app=Flask(__name__)

# index
@app.route('/')
def index():
    grupo = "IDGS803"
    lista =["Juan","Pedro","Carlos"]
    # agregar una pagina por medio del nombre del archivo   
    # para mandarlo a la vista
    return render_template("index.html",grupo=grupo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/OperasBas",methods=["GET"])
def ejemplo3():
    return render_template("OperasBas.html")

@app.route("/OperasBas",methods=["POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        resultado = int(num1)+int(num2)
        
        return render_template("OperasBas.html",resultado = resultado,n1 = num1, n2 = num2)

@app.route("/cinepolis",methods=["GET","POST"])
def cine():
    if request.method == "GET":
        return render_template("cinepolis.html")
    if request.method == "POST":
        num_compradores = request.form.get("compradores")
        num_boletos = request.form.get("boletos")
        tarjeta = request.form.get("radiobtn")
        posibles_compras = int(num_compradores) * 7
        valor = ""
        if int(num_boletos) > posibles_compras:
            valor = "Solo es posible comprar 7 boletos por persona"
        else: 
            valor = int(num_boletos) * 12.00
            if int(num_boletos) > 5:
                valor = valor - (0.15 * valor)
            elif int(num_boletos) > 2:
                valor = valor - (0.10 * valor)
            if tarjeta == "Si":
                valor = valor - (0.10 * valor)
        return render_template("cinepolis.html",valor = valor)
        

@app.route("/hola")
def hola():
    return "Hola!!!"

# va a recibir un parametro de tipo String
@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

# recibe un número entero como parametro
@app.route("/numero/<int:n>")
def numero(n):
    return "Numero {}".format(n)

# los metodos tiene que cambiar si una ruta es igual para dos métodos
@app.route("/user/<string:user>/<int:id>")
def username(user,id):
    return f"Nombre: {user} ID: {id}!!!"

# pasando dos número flotantes para regresar la suma de dichos números
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}!!!".format(n1+n2)

# podria pasar algo o no como parametro
@app.route("/default")
@app.route("/default/<string:nom>")
def func(nom="pedro"):
    return "El nombre de Nom es "+nom

# 
@app.route("/form1")
def form1():
    return '''
        <form>
            <label> Nombre: </label>
            <input type="text" name="nombre" placeholder = "Nombre">
            </br>
            <label> Nombre: </label>
            <input type="text" name="nombre" placeholder = "Nombre">
            </br>
            <label> Nombre: </label>
            <input type="text" name="nombre" placeholder = "Nombre">
            </br>
        </form>
    '''
    

# ahora esta en el puerto 300
if __name__ == '__main__':
    app.run(debug=True,port=300)