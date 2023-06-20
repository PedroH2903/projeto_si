# Importar as classes relevantes

from flask import Flask, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from register_route import registro_bp # Importe o blueprint de registro
from db import Pessoa


app = Flask(__name__)

@app.before_request
def activate_service_worker():
    # Definir as configurações para o Service Worker
    request.environ['wsgi.url_scheme'] = 'https'
    request.environ['HTTP_SERVICE_WORKER_ALLOWED'] = '/'

app.register_blueprint(registro_bp)  # Registrar o blueprint de registro na aplicação Flask

@app.route('/', methods=['GET', 'POST'])
def index():
    # Rota principal
    return render_template('index.html')

app.secret_key = '342342354525351sadad1eqd'  # Chave secreta para gerar sessões seguras

# Configure o banco de dados
engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtenha os dados do formulário de login
        hash_email = request.form['hash_email']
        hash_passw = request.form['hash_passw']
        
        # Inicie uma nova sessão do SQLAlchemy
        db_session = Session()

        # Consulte o banco de dados para encontrar o usuário com as credenciais fornecidas
        user = db_session.query(Pessoa).filter_by(hash_email=hash_email, hash_passw=hash_passw).first()
        
        if user:
            # Se as credenciais forem válidas, salve o usuário na sessão
            session['user_id'] = Pessoa.idpessoa
            session['username'] = Pessoa.name
            
            # Redirecione para a página de sucesso após o login
            return redirect('/home')
        else:
            # Exiba uma mensagem de erro caso as credenciais sejam inválidas
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render_template('login.html', error=error_message)
    
    # Exiba a página de login
    return render_template('login.html')

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

