from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    dados_luiz = {"nome":"Luiz", "idade":"18"}
    dados = {"nome":"Barbara","email":"barbara@gmail.com"}
    lista_alunos = ["André", "Luiz", "Davi", "Lorenzo"]
    nota = 2
    return render_template("index.html", dados_luiz=dados_luiz, dados=dados, lista_alunos=lista_alunos, nota=nota)

if __name__ == "__main__":
    app.run(debug=True)