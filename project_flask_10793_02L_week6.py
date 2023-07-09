#1º passo confirmar a instalação do Flask e fazer o import
from flask import Flask

#neste passo procedemos à criação do site e atribuimos-lhe o nome
app = Flask 
app.config['Challenge_yourself'] = 'desafio'
respostas = ['resposta 1', 'resposta 2', 'resposta 3']
mensagens = []

#adicionamos um decorador que tem como função criar o caminho até ao nosso site, e tem que estar ligado a uma função
@app.route("/") 
def home():
    return 'Olá, estás na página do desafio, estás preparado(a)'
    app.run()