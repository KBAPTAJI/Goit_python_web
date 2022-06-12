from abc import ABC, abstractclassmethod
import json
import pickle


class Meta(type):

    def __call__(cls, *args):
        instance = object.__new__(cls)
        instance.__init__(*args)
        return instance

    def __init__(self, children_number):
        self.children_number = children_number
        self.children_number += 1
        return self.children_number


class SerializationInterface(ABC):

    @abstractclassmethod
    def save_file_json(self):
        pass

    @abstractclassmethod
    def save_file_json_bin(self):
        pass


Meta.children_number = 0


class Cls1(SerializationInterface):

    def __init__(self, data):
        self.data = data

    def save_file_json(self):
        print('Upload to json...')
        with open('cls1.json', 'w') as file:
            json.dump(self.data, file)
        print(f'file{file} has been uploaded')

    def save_file_json_bin(self):
        print('Upload to json_bin...')
        with open('cls1.bin', 'wb') as file:
            pickle.dump(self.data, file)
        print(f'file{file} has been uploaded')
    Meta.children_number += 1


class Cls2(SerializationInterface):

    def __init__(self, data):
        self.data = data

    def save_file_json(self):
        print('Upload to json...')
        with open('cls2.json', 'w') as file:
            json.dump(self.data, file)
        print(f'file{file} has been uploaded')

    def save_file_json_bin(self):
        print('Upload to json_bin...')
        with open('cls2.bin', 'wb') as file:
            pickle.dump(self.data, file)
        print(f'file{file} has been uploaded')
    Meta.children_number += 1


def main():
    char1 = Cls1('data1')
    char2 = Cls1('data2')
    char1.save_file_json()
    char1.save_file_json_bin()
    char2.save_file_json()
    char2.save_file_json_bin()
    print(Meta.children_number)


if __name__ == '__main__':
    main()
