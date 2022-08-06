from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker, joinedload, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "mysql+mysqlconnector://root:pass@127.0.0.1:3306/book_sql_db", echo=True)

session = sessionmaker(bind=engine)()

Base = declarative_base()


class Phones(Base):

    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String(13))
    contact_name_id = Column(Integer, ForeignKey('contact.id'))


class Emails(Base):

    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column(String(56))
    contact_name_id = Column(Integer, ForeignKey('contact.id'))


class Contact(Base):

    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    birthday = Column(String(10))


Base.metadata.bind = engine

new_user1 = Contact(id=1, name='Roma', birthday='24.01.1993')
session.add(new_user1)

new_user1_phone = Phones(id=1, phone='+380630408954', contact_name_id=1)
session.add(new_user1_phone)

new_user1_email = Emails(id=1, email='roma@gmail.com', contact_name_id=1)
session.add(new_user1_email)

session.commit()

for user in session.query(Contact).options(joinedload('Phones')):
    print(user.name)
