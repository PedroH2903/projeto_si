from flask import Flask, render_template, request, current_app
app = Flask(__name__)




@app.before_request
def activate_service_worker():
    request.environ['wsgi.url_scheme'] = 'https'
    request.environ['HTTP_SERVICE_WORKER_ALLOWED'] = '/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        email = request.form.get('email')
        if email.endswith('@aluno.unb.br'):
            # E-mail válido da faculdade, continuar com o processo de login
            return "Sua conta foi criada!"
        else:
            # E-mail inválido, exibir mensagem de erro
            return "E-mail inválido da faculdade. Por favor, insira um e-mail válido."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
