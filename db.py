
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import PasswordType, force_auto_coercion
from sqlalchemy.dialects.mysql import INTEGER

force_auto_coercion()

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    idpessoa = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    registration = Column(String(30, collation='latin1_general_ci'))
    hash_passw = Column(String(1000, collation='latin1_general_ci'))
    name = Column(String(1000, collation='latin1_general_ci'))
    hash_email = Column(String(1000, collation='latin1_general_ci'))


class Categoria(Base):
    __tablename__ = 'categoria'
    id_categoria = Column(Integer, primary_key=True)
    nome = Column(String(500))
    desc = Column(String(1000))

class Item(Base):
    __tablename__ = 'item'
    idobject = Column(Integer, primary_key=True)
    name = Column(String(500))
    model_color = Column(String(500))
    brand_species = Column(String(500))
    year_acquired = Column(String(500))
    desc = Column(String(1000))
    category_idcategory = Column(Integer, ForeignKey('categoria.id_categoria'))
    condition = Column(String(500))
    vaccines = Column(String(500))
    # idade = Column(String(500))
    categoria = relationship('Categoria', backref='itens')

class Pessoa_anuncia_troca_item(Base):
    __tablename__ = 'pessoa_anuncia_troca_item'
    idPessoa_anuncia_troca_item = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.idobject'))
    pessoa_id = Column(Integer, ForeignKey('pessoa.idpessoa'))
    nome = Column(String(500))
    desc = Column(String(1000))
    entrega = Column(String(1000))
    motivo = Column(String(500))
    preco_mercado = Column(String(10))
    listado = Column(Boolean)
    pessoa = relationship('Pessoa', backref='anuncios_troca')
    item = relationship('Item', backref='anuncios_troca')

class Pessoa_anuncia_doa_item(Base):
    __tablename__ = 'pessoa_anuncia_doa_item'
    idPessoa_anuncia_doa_item = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.idobject'))
    pessoa_id = Column(Integer, ForeignKey('pessoa.idpessoa'))
    nome = Column(String(500))
    desc = Column(String(1000))
    entrega = Column(String(1000))
    motivo = Column(String(500))
    listado = Column(Boolean)
    pessoa = relationship('Pessoa', backref='anuncios_doacao')
    item = relationship('Item', backref='anuncios_doacao')

class Pais(Base):
    __tablename__ = 'pais'
    idPais = Column(Integer, primary_key=True)
    nome = Column(String(500))

class UF(Base):
    __tablename__ = 'uf'
    idUf = Column(Integer, primary_key=True)
    pais_id = Column(Integer, ForeignKey('pais.idPais'))
    nome = Column(String(500))
    pais = relationship('Pais', backref='ufs')

class Cidade(Base):
    __tablename__ = 'cidade'
    idCidade = Column(Integer, primary_key=True)
    uf_id = Column(Integer, ForeignKey('uf.idUf'))
    pais_id = Column(Integer, ForeignKey('pais.idPais'))
    nome = Column(String(1000))
    pais = relationship('Pais', backref='cidades')
    uf = relationship('UF', backref='cidades')

class Logradouro(Base):
    __tablename__ = 'logradouro'
    idLogradouro = Column(Integer, primary_key=True)
    cidade_id = Column(Integer, ForeignKey('cidade.idCidade'))
    uf_id = Column(Integer, ForeignKey('uf.idUf'))
    pais_id = Column(Integer, ForeignKey('pais.idPais'))
    nome = Column(String(1000))
    cidade = relationship('Cidade', backref='logradouros')
    uf = relationship('UF', backref='logradouros')
    pais = relationship('Pais', backref='logradouros')

class Endereco(Base):
    __tablename__ = 'endereco'
    idEndereco = Column(Integer, primary_key=True)
    pessoa_id = Column(Integer, ForeignKey('pessoa.idpessoa'))
    logradouro_id = Column(Integer, ForeignKey('logradouro.idLogradouro'))
    cidade_id = Column(Integer, ForeignKey('cidade.idCidade'))
    uf_id = Column(Integer, ForeignKey('uf.idUf'))
    pais_id = Column(Integer, ForeignKey('pais.idPais'))
    desc = Column(String(1000))
    pessoa = relationship('Pessoa', backref='enderecos')
    logradouro = relationship('Logradouro', backref='enderecos')
    cidade = relationship('Cidade', backref='enderecos')
    uf = relationship('UF', backref='enderecos')
    pais = relationship('Pais', backref='enderecos')
