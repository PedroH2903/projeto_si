from flask import Blueprint, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Pessoa  # Importe as classes relevantes

login_bp = Blueprint('login', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
db_session = Session()

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtenha os dados do formulário de login
        hash_email = request.form['hash_email']
        hash_passw = request.form['hash_passw']

        # Consulte o banco de dados para verificar se o usuário existe
        pessoa = db_session.query(Pessoa).filter_by(hash_email=hash_email).first()

        if pessoa and pessoa.hash_passw == hash_passw:
            # Autenticação bem-sucedida
            session['user_id'] = pessoa.idpessoa
            session['username'] = pessoa.name
            return redirect('/home')
        else:
            # Autenticação falhou
            return render_template('login.html', error=True)

    return render_template('login.html', error=False)
