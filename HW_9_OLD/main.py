from connect_db import session
from models import Contact


def get_contact():
    contact = session.query(Contact).all()

    for con in contact:
        print('----------------')
        print(f'Name:{con.name}, birthday: {con.birthday}')
        print('////////////////')


def get_number_phone():
    phone = session.query(Contact).all()
    for ph in phone:
        print('----------------')
        print(f'Name:{ph.name}, phone:{ph.phone}')
        print('////////////////')


def main():
    # get_contact()
    get_number_phone()


if __name__ == '__main__':
    main()
