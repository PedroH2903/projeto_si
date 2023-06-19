from flask import Blueprint, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Pessoa  # Importe as classes relevantes

registro_bp = Blueprint('registro', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
session = Session()
ultima_pessoa = session.query(Pessoa).order_by(Pessoa.idpessoa.desc()).first()
ultimo_id = ultima_pessoa.idpessoa

@registro_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        # Obtenha os dados do formulário de registro
        registration = request.form['registration']
        hash_passw = request.form['hash_passw']
        name = request.form['name']
        hash_email = request.form['hash_email']

        # Crie uma nova instância da classe Pessoa com os dados do formulário
        nova_pessoa = Pessoa(idpessoa=ultimo_id+1, registration=registration, hash_passw=hash_passw, name=name, hash_email=hash_email)

        # Inicie uma nova sessão do SQLAlchemy
        try:
            # Adicione a nova pessoa à sessão
            session.add(nova_pessoa)

            # Faça o commit da sessão para salvar a nova pessoa no banco de dados
            session.commit()

            # Redirecione para uma página de sucesso ou faça algo similar
            return redirect('/registro_sucesso')

        except Exception as e:
            # Lide com possíveis erros durante o registro
            session.rollback()
            print(f"Erro durante o registro: {str(e)}")
            return render_template('registrar.html', error=True)

        finally:
            # Feche a sessão do SQLAlchemy
            session.close()

    return render_template('registrar.html', error=False)
