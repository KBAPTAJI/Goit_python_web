from faker import Faker
from connect_db import session
from models import Contact

fake = Faker()


def create_contacts():
    for _ in range(1, 6):
        contact = Contact(
            name=fake.first_name(),
            birthday=fake.date(),
            email=fake.ascii_free_email(),
            phone_work=fake.phone_number(),
            phone_home=fake.phone_number(),
            phone_mobile=fake.phone_number(),
        )
        session.add(contact)
    session.commit()


def main():
    create_contacts()


if __name__ == '__main__':
    main()
