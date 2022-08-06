import imp
import random

from faker import Faker

from connect_db import session
from models import Contact, Phones, Con_Phon

fake = Faker()


def create_contacts():
    for _ in range(1, 6):
        contact = Contact(
            name=fake.first_name(),
            birthday=fake.date(),
            email=fake.ascii_free_email(),
        )
        session.add(contact)
    session.commit()


def create_phones():
    phones = Phones(phone='+380674445566')
    session.add(phones)
    phones = Phones(phone='+380673333333')
    session.add(phones)
    phones = Phones(phone='+380674465433')
    session.add(phones)
    session.commit()


def create_Con_Phon():
    con = 1
    phon = 1
    relation = Con_Phon(contact=con, phone=phon)
    session.add(relation)

    con = 1
    phon = 2
    relation = Con_Phon(contact=con, phone=phon)
    session.add(relation)

    con = 2
    phon = 3
    relation = Con_Phon(contact=con, phone=phon)
    session.add(relation)
    session.commit()


def main():
    # create_contacts()
    # create_phones()
    create_Con_Phon()


if __name__ == '__main__':
    main()
