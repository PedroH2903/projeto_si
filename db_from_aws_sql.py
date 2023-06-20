from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    idpessoa = Column(Integer, primary_key=True)
    registration = Column(String(100, collation='big5'))
    hash_passw = Column(String(1000))
    name = Column(String(200))
    hash_email = Column(String(1000))


class Category(Base):
    __tablename__ = 'category'

    idcategory = Column(Integer, primary_key=True)
    name = Column(String(450))
    desc = Column(String(100))


class Item(Base):
    __tablename__ = 'item'

    idobject = Column(Integer, primary_key=True)
    name = Column(String(45))
    model_color = Column(String(45))
    brand_species = Column(String(45))
    year_acquired = Column(String(45))
    desc = Column(String(45))
    category_idcategory = Column(Integer, ForeignKey('category.idcategory'))
    condition = Column(String(45))
    vaccines = Column(String(45))
    likes = Column(String(45))
    dislikes = Column(String(45))

    category = relationship('Category')


class PersonAdvExchItem(Base):
    __tablename__ = 'person_adv_exch_item'

    person_idpessoa = Column(Integer, ForeignKey('person.idpessoa'), primary_key=True)
    object_idobject = Column(Integer, primary_key=True)
    object_category_idcategory = Column(Integer, primary_key=True)
    desc = Column(String(45))
    exch_for = Column(String(45))
    delivery = Column(String(45))
    reason = Column(String(45))
    market_price = Column(String(45))
    listed = Column(String(45))

    person = relationship('Person')
    item = relationship('Item', primaryjoin='and_(Item.idobject == foreign(PersonAdvExchItem.object_idobject), '
                                           'Item.category_idcategory == foreign(PersonAdvExchItem.object_category_idcategory))')


class PersonAdvDonateItem(Base):
    __tablename__ = 'person_adv_donate_item'

    person_idpessoa = Column(Integer, ForeignKey('person.idpessoa'), primary_key=True)
    object_idobject = Column(Integer, primary_key=True)
    object_category_idcategory = Column(Integer, primary_key=True)
    desc = Column(String(45))
    delivery = Column(String(45))
    reason = Column(String(45))
    listed = Column(String(45))

    person = relationship('Person')
    item = relationship('Item', primaryjoin='and_(Item.idobject == foreign(PersonAdvDonateItem.object_idobject), '
                                           'Item.category_idcategory == foreign(PersonAdvDonateItem.object_category_idcategory))')


class Country(Base):
    __tablename__ = 'country'

    idcountry = Column(Integer, primary_key=True)
    name = Column(String(45))


class FU(Base):
    __tablename__ = 'FU'

    idFU = Column(Integer, primary_key=True)
    name = Column(String(45))
    country_idcountry = Column(Integer, ForeignKey('country.idcountry'))

    country = relationship('Country')


class City(Base):
    __tablename__ = 'city'

    idcity = Column(Integer, primary_key=True)
    name = Column(String(45))
    FU_idFU = Column(Integer)
    FU_country_idcountry = Column(Integer)

    fu = relationship('FU', primaryjoin='and_(FU.idFU == foreign(City.FU_idFU), '
                                        'FU.country_id')
