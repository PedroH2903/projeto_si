#UNB 23/1 SI G1 https://github.com/PedroH2903/projeto_si
#!TODO: classificar relacionamentos em one-to-many, etc, e usar passwordType na autenticacao de usuario
from sqlalchemy import Column,ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.password import PasswordType
from sqlalchemy_utils import force_auto_coercion

force_auto_coercion()

Base = declarative_base()

#classe
    #nome tabela
    #chaves
    #atributos
    #relationships

class Pessoa(Base):
    __tablename__ = 'pessoa'
    idpessoa = Column(Integer, primary_key=True)

    matricula = Column(String(30))
    senha = Column(String(1000)) #!TODO: use PasswordType
    nome = Column(String(1000), collation='latin1')
    email = Column(String(1000))

class Categoria(Base):
    __tablename__='categoria'
    id_categoria = Column(Integer, primary_key=True)

    nome = Column(String(500))
    desc = Column(String(1000))

class Item(Base):
    __tablename__='item'
    id_item = Column(Integer, primary_key=True)

    nome = Column(String(500))
    desc = Column(String(1000))
    modelo_cor = Column(String(500))
    marca_especie = Column(String(500))
    idade = Column(String(500))
    condicao = Column(String(500))
    vacinas = Column(String(500))
    categoria_idCategoria = Column(Integer, ForeignKey('categoria.idCategoria'))

    categoria = relationship('Categoria') #!TODO: definir one to many, many to many etc??


class Pessoa_anuncia_troca_item(Base):
    __tablename__='pessoa_anuncia_troca_item'
    idPessoa_anuncia_troca_item = Column(Integer, primary_key=True)
    item_idItem = Column(Integer, primary_key=True)
    item_categoria_idCategoria = Column(Integer, primary_key=True)

    nome = Column(String(500))
    desc = Column(String(1000))
    entrega = Column(String(1000))
    motivo =Column(String(500))
    preco_merado = Column(String(10))
    #isListado = Column(Boolean, unique=False, default=True)
    listado = Column(Boolean(10))

    pessoa = relationship('Pessoa') #!TODO: definir one to many, many to many etc??
    item = relationship('Item') #!TODO: definir one to many, many to many etc??

class Pessoa_anuncia_doa_item(Base):
    __tablename__='pessoa_anuncia_doa_item'
    idPessoa_anuncia_doa_item = Column(Integer, primary_key=True)
    item_idItem = Column(Integer, primary_key=True)
    item_categoria_idCategoria = Column(Integer, primary_key=True)

    nome = Column(String(500))
    desc = Column(String(1000))
    entrega = Column(String(1000))
    motivo =Column(String(500))
    listado = Column(String(10))

    pessoa = relationship('Pessoa') #!TODO: definir one to many, many to many etc??
    item = relationship('Item') #!TODO: definir one to many, many to many etc??

class Pais(Base):
    __tablename__='pais'
    idPais = Column(Integer, primary_key=True)
    nome = Column(String(500))

class UF(Base):
    __tablename__='uf'
    idUf = Column(Integer, primary_key=True)
    pais_idPais = Column(Integer, primary_key=True)

    nome = Column(String(500))

    pais = relationship('Pais')

class Cidade(Base):
    __tablename__='cidade'
    idCidade = Column(Integer, primary_key=True)
    uf_idUf = Column(Integer, primary_key=True)
    pais_idPais = Column(Integer, primary_key=True)

    nome = Column(String(1000))

    pais = relationship('Pais')
    cidade = relationship('Cidade')



class Logradouro(Base):
    __tablename__=('logradouro')
    idLogradouro = Column(Integer, primary_key=True)
    cidade_idCidade = Column(Integer, primary_key=True)
    uf_idUf = Column(Integer, primary_key=True)
    pais_idPais = Column(Integer, primary_key=True)

    nome = Column(String(1000))

    cidade = relationship('Cidade')
    uf = relationship('Uf')
    pais = relationship('Pais')

class Endereco(Base):
    __tablename__='endereco'
    idEndereco = Column(Integer, primary_key=True)
    pessoa_idPessoa = Column(Integer, primary_key=True)
    idLogradouro = Column(Integer, primary_key=True)
    cidade_idCidade = Column(Integer, primary_key=True)
    uf_idUf = Column(Integer, primary_key=True)
    pais_idPais = Column(Integer, primary_key=True)

    desc = Column(String(1000))

    pessoa = relationship('Pessoa')
    cidade = relationship('Cidade')
    uf = relationship('Uf')
    pais = relationship('Pais')
