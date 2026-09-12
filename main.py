from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        app.static_folder,
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon"
    )

@app.route("/operacao", methods=["GET", "POST"])
def operacao():

    if request.method == "POST":

        numero1 = float(request.form["numero1"])
        numero2 = float(request.form["numero2"])
        operador = request.form["operador"]

        if operador == "+":
            resultado = numero1 + numero2

        elif operador == "-":
            resultado = numero1 - numero2

        elif operador == "*":
            resultado = numero1 * numero2

        elif operador == "/":
            if numero2 == 0:
                return "Não é possível dividir por zero!"

            resultado = numero1 / numero2

        else:
            return "Operador inválido!"

        return render_template(
            "resultado.html",
            numero1=numero1,
            numero2=numero2,
            operador=operador,
            resultado=resultado
        )

    return render_template("operacao.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False
    )
