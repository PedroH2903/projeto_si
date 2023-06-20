# Importar as classes relevantes

from flask import Flask, render_template, request, redirect, session
from register_route import registro_bp # Importe o blueprint de registro
from login_route import login_bp


app = Flask(__name__)

@app.before_request
def activate_service_worker():
    # Definir as configurações para o Service Worker
    request.environ['wsgi.url_scheme'] = 'https'
    request.environ['HTTP_SERVICE_WORKER_ALLOWED'] = '/login'

app.register_blueprint(registro_bp)  # Registrar o blueprint de registro na aplicação Flask

app.register_blueprint(login_bp)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Rota principal
    return render_template('index.html')

app.secret_key = '342342354525351sadad1eqd'  # Chave secreta para gerar sessões seguras

# Configure o banco de dados

@app.route('/logout')
def logout():
    # Remova as informações do usuário da sessão
    session.pop('user_id', None)
    session.pop('username', None)
    
    # Redirecione para a página de login
    return redirect('/login')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

