
from flask import Flask

#neste passo procedemos à criação do site e atribuimos-lhe o nome
app = Flask 
app.config['Challenge_yourself'] = 'desafio'
respostas = ['resposta 1', 'resposta 2', 'resposta 3']
mensagens = []


#1º passo confirmar a instalação do Flask e fazer o import
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['Challenge_yourself'] = 'desafio'
respostas = ['resposta 1', 'resposta 2', 'resposta 3']
mensagens = []

@app.route("/") #adicionei um decorador que tem como função criar o caminho até ao nosso site, e tem que estar ligado a uma função. Neste projeto vamos criar 3, correspondentes a 3 desafios.
def home():
    return render_template('index.html')

@app.route("/desafio1", methods=['GET', 'POST'])
def desafio1():
    if request.method == 'POST':
        resposta = request.form['resposta']
        if resposta == respostas[0]:
            mensagem = 'Desafio 1 concluído com sucesso!'
        else:
            mensagem = 'Resposta incorreta! Tente novamente.'
        mensagens.append(mensagem)
        return render_template('resultado.html', mensagem=mensagem)
    return render_template('desafio1.html')

@app.route("/desafio2", methods=['GET', 'POST'])
def desafio2():
    if request.method == 'POST':
        resposta = request.form['resposta']
        if resposta == respostas[1]:
            mensagem = 'Desafio 2 concluído com sucesso!'
        else:
            mensagem = 'Resposta incorreta! Tente novamente.'
        mensagens.append(mensagem)
        return render_template('resultado.html', mensagem=mensagem)
    return render_template('desafio2.html')

@app.route("/desafio3", methods=['GET', 'POST'])
def desafio3():
    if request.method == 'POST':
        resposta = request.form['resposta']
        if resposta == respostas[2]:
            mensagem = 'Desafio 3 concluído com sucesso!'
        else:
            mensagem = 'Resposta incorreta! Tente novamente.'
        mensagens.append(mensagem)
        return render_template('resultado.html', mensagem=mensagem)
    return render_template('desafio3.html')

if __name__ == '__main__':
    app.run()