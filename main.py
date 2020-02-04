from flask import Flask, request, render_template

def create_app ():

    app = Flask(__name__)

    @app.route("/")
    def home():
        n1 = 43
        n2 = 76
        soma = n1 + n2
        return render_template('index.html', var1=soma, var2='Alessandro')

    @app.route("/produtos")
    def produtos():
        x = request.args.get("id")
        y = request.args.get("nome")

        lista_frutas = ('Maca', 'Uva', 'Pera')

        return render_template('produtos.html', frutas=lista_frutas, n1=33)

    @app.route("/detalhes")
    def detalhes():
        x = request.args.get("item")
        return render_template('detalhes.html', item =x)



    return app


app = create_app()

app.run(debug=True, port=2000, host="localhost")