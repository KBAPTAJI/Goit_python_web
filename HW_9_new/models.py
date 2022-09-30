from connect_db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Contact(Base):

    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    birthday = Column(String(30))
    email = Column(String(100))
    phone_work = Column(String(100))
    phone_home = Column(String(100))
    phone_mobile = Column(String(100))
