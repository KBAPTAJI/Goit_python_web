from connect_db import session
from sqlalchemy.orm import joinedload
from models import Con_Phon, Contact, Phones


def get_contact():
    contact = session.query(Contact).options(joinedload('phone')).all()

    for con in contact:
        print('----------------')
        print(f'Name:{con.name}, birthday: {con.birthday}, email: {con.email}')
        for c in con.phone:
            if c is not None:
                print(f'Tel: {c.phone}')
        print('////////////////')


def get_number_phone():
    phone = session.query(Contact).options(
        joinedload('phone')).filter_by(id=1)
    print(phone)
    for ph in phone:
        print('----------------')
        print(f'Name:{ph.name}')
        for p in ph.phone:
            print(f'Phone: {p.phone}')
        print('////////////////')


def main():
    # get_contact()
    get_number_phone()


if __name__ == '__main__':
    main()
