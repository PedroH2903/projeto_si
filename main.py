from flask import Flask, render_template, request, redirect, session
from register_route import registro_bp # Importe o blueprint de registro
from login_route import login_bp
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from register_route import registro_bp # Importe o blueprint de registro
from orm_db_trocatroca_210723 import *
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
engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtenha os dados do formulário de login
        email = request.form['email']
        passw = request.form['passw']
        
        # Inicie uma nova sessão do SQLAlchemy
        db_session = Session()

        # Consulte o banco de dados para encontrar o usuário com as credenciais fornecidas
        user = db_session.query(Person).filter_by(email=email, passw=passw).first()
        
        if user:
            # Se as credenciais forem válidas, salve o usuário na sessão
            session['user_id'] = Person.idperson
            session['username'] = Person.name
            
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
    # Verifique se o usuário está logado
    if 'user_id' in session:
        # Recupere as informações do usuário da sessão
        user_id = session['user_id']
        username = session['username']
        
        # Exiba as informações do usuário na página de boas-vindas
        return render_template('home.html', username=username)
    else:
        # Se o usuário não estiver logado, redirecione para a página de login
        return redirect('/login')
    

@app.route('/items')
def display_items():
    db = Session()
    items = db.query(Item).all()
    db.close()  
    return render_template('items.html', items=items)

@app.route('/image/<item_id>')
def display_image(item_id):
    db = Session()
    item = db.query.get(item_id)
    # item = Item.query.get(item_id)
    if item and item.image_blob:
        image_base64 = base64.b64encode(item.image_blob).decode('utf-8')
        return f'<img src="data:image/jpeg;base64,{image_base64}" alt="Item Image">'
    else:
        return 'Image not found'
    db.close()



if __name__ == '__main__':
    app.run(debug=True)

