
from calendar import month
from collections import UserDict
from datetime import date, datetime, timedelta
import re
from flask import Flask


class AdressBook(UserDict):

    def __init__(self, dict_book={}):
        self.dict_book = dict_book


class Field:
    pass


class Name:

    def __init__(self, name):
        self.name = name


class Phone:

    def __init__(self, phone):
        self.phone = phone

    def set_tel_number(self):
        if self.phone == '':
            return None
        else:
            result = self.sanitize_phone_number()
            if result == '':
                return None
            else:
                return result

    def sanitize_phone_number(self,):
        total_str_number = ''
        number = re.findall('\d', self.phone)
        my_string = ''.join(number)
        if len(my_string) < 10:
            print('input correct phone')
        elif len(my_string) == 10:
            total_str_number += '+38'
            total_str_number += my_string
        else:
            total_str_number += '+'
            total_str_number += my_string
        return total_str_number


class Birthday:

    def __init__(self, birthday):
        self.birthday = birthday

    def birthday_strptime(self,):
        result = datetime.strptime(self.birthday, '%d.%m.%Y')
        return result


class Email:

    def __init__(self, email):
        self.email = email

    def find_all_emails(self,):
        result = re.findall(
            r"[a-zA-Z]{1}[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,3}", self.email)
        return result


class Record:
    def __init__(self,):
        self.list_of_tel = []
        self.birthday = []
        self.email = []
        self.total_list = [self.list_of_tel, self.birthday, self.email]

    def add_contact(self, Name, Phone):
        # print(AdressBook.dict_book)
        if AdressBook().dict_book == {}:
            # print('I m empty')
            if Phone.set_tel_number() == None:
                book1 = AdressBook().dict_book[Name.name] = self.total_list
                return book1

            else:
                self.list_of_tel.append(Phone.set_tel_number())
                book2 = AdressBook().dict_book[Name.name] = self.total_list
                return book2
        else:
            result = AdressBook().dict_book.get(Name.name)
            if result == None:
                self.list_of_tel.append(Phone.set_tel_number())
                book3 = AdressBook().dict_book[Name.name] = self.total_list
                return book3
            elif result[0] == []:
                self.list_of_tel.append(Phone.set_tel_number())
                book4 = AdressBook().dict_book[Name.name] = self.total_list
                return book4
            else:
                if Phone.set_tel_number() in self.list_of_tel:
                    print(f'tel {Phone.set_tel_number()} exist, input other')
                else:
                    self.reload_AB(result)
                    self.list_of_tel.append(Phone.set_tel_number())
                    AdressBook().dict_book[Name.name] = self.total_list
                    return AdressBook().dict_book

    def remove_contact(self, Name):
        result = AdressBook().dict_book.pop(Name.name)
        return result

    def get_phone_number(self,):
        result = AdressBook().dict_book.get(self.name)
        print(result[0])
        return result

    def get_birthday(self,):
        result = AdressBook().dict_book.get(self.name)
        print(result[1])
        return result

    def get_email(self,):
        result = AdressBook().dict_book.get(self.name)
        print(result[2])
        return result

    def remove_number(self, Name, Phone):
        get_phone = AdressBook().dict_book.get(Name.name)
        new_list = []
        for elem in get_phone[0]:
            if elem == None:
                new_list = []
            elif elem == Phone.phone:
                print(f'{elem} - deleted')
            else:
                new_list.append(elem)
        self.reload_remove(get_phone, new_list)
        result = AdressBook().dict_book[Name.name] = self.total_list
        return result

    def remove_email(self, Name, Email):
        get_email = AdressBook().dict_book.get(Name.name)
        new_list = []
        for elem in get_email[2]:
            if elem == None:
                new_list = []
            elif elem == Email.email:
                print(f'{elem} - deleted')
            else:
                new_list.append(elem)
        self.reload_remove_email(get_email, new_list)
        AdressBook().dict_book[Name.name] = self.total_list

    def remove_birthday(self, Name, Birthday):
        get_birthday = AdressBook().dict_book.get(Name.name)
        new_list = []
        for elem in get_birthday[1]:
            if elem == None:
                new_list = []
            elif elem == Birthday.birthday:
                print(f'{elem} - deleted')
            else:
                new_list.append(elem)
        self.reload_remove_birthday(get_birthday, new_list)
        AdressBook().dict_book[Name.name] = self.total_list

    def reload_AB(self, result):
        for elem in result[0]:
            if isinstance(elem, list):
                for el in elem:
                    self.list_of_tel.append(el)
            else:
                self.list_of_tel.append(elem)
        for elem in result[1]:
            if isinstance(elem, list):
                for el in elem:
                    self.birthday.append(el)
            else:
                self.birthday.append(elem)
        for elem in result[2]:
            if isinstance(elem, list):
                for el in elem:
                    self.email.append(el)
            else:
                self.email.append(elem)

    def reload_remove(self, result, new_list):
        for elem in new_list:
            if isinstance(elem, list):
                for el in elem:
                    self.list_of_tel.append(el)
            else:
                self.list_of_tel.append(elem)
        for elem in result[1]:
            if isinstance(elem, list):
                for el in elem:
                    self.birthday.append(el)
            else:
                self.birthday.append(elem)
        for elem in result[2]:
            if isinstance(elem, list):
                for el in elem:
                    self.email.append(el)
            else:
                self.email.append(elem)

    def reload_remove_birthday(self, result, new_list):
        for elem in result[0]:
            if isinstance(elem, list):
                for el in elem:
                    self.list_of_tel.append(el)
            else:
                self.list_of_tel.append(elem)
        for elem in new_list:
            if isinstance(elem, list):
                for el in elem:
                    self.birthday.append(el)
            else:
                self.birthday.append(elem)
        for elem in result[2]:
            if isinstance(elem, list):
                for el in elem:
                    self.email.append(el)
            else:
                self.email.append(elem)

    def reload_remove_email(self, result, new_list):
        for elem in result[0]:
            if isinstance(elem, list):
                for el in elem:
                    self.list_of_tel.append(el)
            else:
                self.list_of_tel.append(elem)
        for elem in result[1]:
            if isinstance(elem, list):
                for el in elem:
                    self.birthday.append(el)
            else:
                self.birthday.append(elem)
        for elem in new_list:
            if isinstance(elem, list):
                for el in elem:
                    self.email.append(el)
            else:
                self.email.append(elem)

    def add_email(self, Name, Email):
        result = AdressBook().dict_book.get(Name.name)
        self.reload_AB(result)
        self.email.append(Email.find_all_emails())
        book5 = AdressBook().dict_book[Name.name] = self.total_list
        return book5

    def add_birthday(self, Name, Birthday):
        result = AdressBook().dict_book.get(Name.name)
        self.reload_AB(result)
        self.birthday.append(Birthday.birthday)
        book6 = AdressBook().dict_book[Name.name] = self.total_list
        return book6

    def days_to_birthday(self, Name):
        get_name = AdressBook().dict_book.get(Name.name)
        time = Birthday(get_name[1][0]).birthday_strptime()
        current_time = datetime.now()
        year_delta = timedelta(days=365)
        year_delta_top = timedelta(days=365)
        time_delta = datetime(year=current_time.year, month=time.month, day=time.day) - \
            datetime(year=current_time.year,
                     month=current_time.month, day=current_time.day)
        day_of_time = timedelta(days=0)
        february_28 = timedelta(days=28)
        if time_delta < day_of_time:
            february = datetime(year=current_time.year, month=2, day=28)
            if february.date == february_28:
                result = time_delta + year_delta
                print(f'{result.days} days left')
                return result
            else:
                result = time_delta + year_delta_top
                print(f'{result.days} days left')
                return result
        elif time_delta > day_of_time:
            print(f'{time_delta.days} days left')
            return time_delta
        else:
            print(f'Day of birthday today')
            return 'Day of birthday today'

    def show_all(self,):
        print(AdressBook().dict_book)
        return AdressBook().dict_book

    def helper(self,):
        print('How can i help you?')
        return 'How can i help you?'

    def goodbye(self,):
        print('Good bye!')
        return 'Good bye!'


app = Flask(__name__)


@app.route('/')
def main():
    while True:
        hello = input('')
        Hello = hello.casefold()
        if Hello == 'hello':
            Record().helper()

        elif Hello == 'good bye' or Hello == 'close' or Hello == 'exit':
            Record().goodbye()
            break

        elif Hello == 'add':
            name, phone = input('Name: '), input('Phone: ')
            Record().add_contact(Name(name), Phone(phone))

        elif Hello == 'phone':
            name = input('Name of contact: ')
            Record.get_phone_number(Name(name))

        elif Hello == 'show all':
            Record().show_all()

        elif Hello == 'remove contact':
            name = input('Name: ')
            Record().remove_contact(Name(name))

        elif Hello == 'remove number':
            name, phone = input('Name: '), input('Phone: ')
            Record().remove_number(Name(name), Phone(phone))

        elif Hello == 'add birthday':
            name, birthday = input('Name: '), input(
                'Format (01.01.2000) - birthday: ')
            Record().add_birthday(Name(name), Birthday(birthday))

        elif Hello == 'remove birthday':
            name, birthday = input('Name: '), input('birthday: ')
            Record().remove_birthday(Name(name), Birthday(birthday))

        elif Hello == 'birthday':
            name = input('Name of contact: ')
            Record.get_birthday(Name(name))

        elif Hello == 'How many days to birthday':
            name = input('Name of contact: ')
            Record().days_to_birthday(Name(name))

        elif Hello == 'add email':
            name, email = input('Name: '), input('email: ')
            Record().add_email(Name(name), Email(email))

        elif Hello == 'remove email':
            name, phone = input('Name: '), input('email: ')
            Record().remove_email(Name(name), Email(email))

        elif Hello == 'email':
            name = input('Name of contact: ')
            Record.get_email(Name(name))

        else:
            print('I don\'t know this command')


if __name__ == '__main__':
    print('Welcome!')
    app.run(debug=True, host='0.0.0.0')
    # main()
