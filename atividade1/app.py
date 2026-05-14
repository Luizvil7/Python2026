from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def decorator():
    return ("""
Um decorator no Flask é um padrão de projeto estrutural, herdado do Python, que permite adicionar funcionalidades extras a uma função (como uma rota) sem modificar seu código original.
No contexto do Flask, eles funcionam como "embalagens inteligentes" (wrappers) que envolvem uma função de visualização (view function) para modificar seu comportamento ou registrar rotas.""")

if __name__ == "__main__":
    app.run(debug=True)