# Importar as classes relevantes

from flask import Flask, render_template, request, redirect, session
from register_route import registro_bp # Importe o blueprint de registro
from login_route import login_bp
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from register_route import registro_bp # Importe o blueprint de registro
from trocatroca0_orm import *
import base64

app = Flask(__name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
session = Session()

@app.before_request
def activate_service_worker():
    # Definir as configurações para o Service Worker
    request.environ['wsgi.url_scheme'] = 'https'
    request.environ['HTTP_SERVICE_WORKER_ALLOWED'] = '/'

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
    items = session.query(Item).all()
    return render_template('home.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)

