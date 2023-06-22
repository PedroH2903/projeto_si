from flask import Blueprint, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_db_trocatroca_210723 import Person  # Importe as classes relevantes

login_bp = Blueprint('login', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
db_session = Session()

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtenha os dados do formulário de login
        email = request.form['email']
        passw = request.form['passw']

        # Consulte o banco de dados para verificar se o usuário existe
        pessoa = db_session.query(Person).filter_by(email=email).first()

        if pessoa and pessoa.passw == passw:
            # Autenticação bem-sucedida
            session['user_id'] = pessoa.idPerson
            session['username'] = pessoa.name
            return redirect('/home')
        else:
            # Autenticação falhou
            return render_template('login.html', error=True)

    return render_template('login.html', error=False)
