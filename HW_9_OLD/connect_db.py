from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

user = config.get('DB', 'user')
password = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

Base = declarative_base
engine = create_engine(
    f'postgresql://{user}:{password}@{domain}:5432/{db_name}', echo=True)


session = sessionmaker(bind=engine)()
