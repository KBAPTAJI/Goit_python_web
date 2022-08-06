from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Phones(Base):

    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String(13))
    contact = relationship(
        'Contact', secondary='con_phon', back_populates='phone')


class Contact(Base):

    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    birthday = Column(String(10))
    email = Column('emailll', String(50))
    phone = relationship(
        'Phones', secondary='con_phon', back_populates='contact')


class Con_Phon(Base):
    __tablename__ = 'con_phon'
    id = Column(Integer, primary_key=True)
    contact = Column('contact', ForeignKey('contact.id'))
    phone = Column('phone', ForeignKey('phones.id'))
