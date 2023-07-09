#pfragoso

#1º passo confirmar a instalação do Flask e fazer o import. da função render_template e do request
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RespostaForm, MensagemForm

#neste passo procedemos à criação da app, atribuimos-lhe o nome e as respostas.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'desafio'
respostas = ['resposta1', 'resposta2', 'resposta3']
mensagens = []

 #adicionei um decorador que tem como função criar o caminho até ao nosso site, e tem que estar ligado a uma função. Neste projeto vamos criar 3, correspondentes a 3 desafios.
@app.route("/", methods=['GET', 'POST'])
def home_desafio():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[0]:
            return redirect(url_for('desafio2'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('home_desafio.html', form=form)

@app.route("/desafio2", methods=['GET', 'POST'])
def desafio2():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[1]:
            return redirect(url_for('desafio3'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafio2.html', form=form)


@app.route("/desafio3", methods=['GET', 'POST'])
def desafio3():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[3]:
            return redirect(url_for('desafio_final'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('desafio3.html', form=form)


@app.route("/desafio_final", methods=['GET', 'POST'])
def desafio_final():
    form = MensagemForm()
    if form.validate_on_submit():
        mensagem = form.mensagem.data
        mensagens.append(mensagem)
        print(f'Mensagem recebida: {mensagem}') # Print da mensagem no terminal
        flash(f'Mensagem enviada com sucesso! Já existem {len(mensagens)} mensagem(s).', 'success')
    return render_template('desafio_final.html', form=form)

@app.route("/mensagens")
def ver_mensagens():
    return render_template('mensagens.html', mensagens=mensagens)
if __name__ == "__main__":
    app.run()


