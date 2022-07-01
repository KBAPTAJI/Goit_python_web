from datetime import datetime
from pathlib import Path
import sys
import os
import re
from threading import Thread
import shutil


my_directory_files = {'изображения': {'.JPEG', '.jpeg', '.png', '.PNG', '.JPG', '.jpg', '.SVG', '.svg'},
                      'видео файлы': {'.avi', '.mp4', '.mov', '.mkv'},
                      'документы': {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX', '.csv', '.CSV'},
                      'музыка': {'.mp3', '.ogg', '.wav', '.amr', '.MP3', '.OGG', '.WAV', '.AMR'},
                      'архивы': {'.zip', '.gz', '.tar', '.ZIP', '.GZ', '.TAR'},
                      'неизвестные расширения': {'.'}
                      }


def normalize(file_name):
    my_rus_alf = 'абвгдеёжзиклмнопрстуфхцчшщьыэюяАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ0123456789'
    my_eng_alf = 'abvgdeejziklmnoprstufhc4hhbieuyABVGDEEJZIKLMNOPRSTUFHC4HHBIEUY0123456789'
    trans = file_name.maketrans(my_rus_alf, my_eng_alf)
    my_new_file_name = file_name.translate(trans)
    return my_new_file_name


def walk_folders(pathroot, new_suffix, files_path, files_stem, files_name):
    for element in pathroot.iterdir():
        if element.is_file():
            print(f'{element.name} - файл')
            add_element(element, new_suffix, files_path,
                        files_stem, files_name)
        else:
            print(f'{element} - папка')
            walk_folders(element, new_suffix, files_path,
                         files_stem, files_name)


def add_element(element, new_suffix, files_path, files_stem, files_name):
    new_suffix.add(element.suffix)
    files_path.append(element)
    files_stem.append(element.stem)
    files_name.append(element.name)
    print(new_suffix, files_path, files_stem, files_name)
    return new_suffix, files_path, files_stem, files_name


def makedir(pathroot, name):
    directory_name = f'{pathroot}\{name}'
    new_path = Path(directory_name)
    try:
        Path.mkdir(new_path)
    except FileExistsError:
        print('Папка уже существует, создавать не надо')


def replace_file(pathroot, name, names):
    try:
        directory_name = f'{pathroot}\{name}'
        new_path = Path(directory_name)
        os.replace(f'{pathroot}\{names}', f'{new_path}\{normalize(names)}')
    except WindowsError:
        print('файл не найден')


def replace_file_archive(pathroot, name, names):
    try:
        directory_name = f'{pathroot}\{name}'
        new_path = Path(directory_name)
        os.replace(f'{pathroot}\{names}', f'{new_path}\{normalize(names)}')
        unpackarchive(new_path, names)
    except WindowsError:
        print('файл не найден')


def unpackarchive(new_path, names):
    shutil.unpack_archive(f'{new_path}\{normalize(names)}', f'{new_path}')


def main():
    if len(sys.argv) < 2:
        print('аргументов меньше 1')
    else:
        start_time = datetime.now()
        pathroot_2 = sys.argv[1]
        pathroot = Path(pathroot_2)
        if pathroot.exists():
            if pathroot.is_dir():
                new_suffix = set()
                files_path = []
                files_stem = []
                files_name = []
                walk_folders(pathroot, new_suffix,
                             files_path, files_stem, files_name)
                # walker_thrade = Thread(target=walk_folders, args=(pathroot, new_suffix,
                #                                                   files_path, files_stem, files_name))
                # walker_thrade.start()

        for name in my_directory_files:
            if name == 'изображения':
                makedir(pathroot, name)
                for key, value in my_directory_files.items():
                    if key == 'изображения':
                        set_of_key = value & new_suffix
                        for elements in set_of_key:
                            for names in files_name:
                                if elements in names:
                                    image_thrade = Thread(target=replace_file, args=(
                                        pathroot, name, names))
                                    image_thrade.start()
                try:

                    directory_name = f'{pathroot}\{name}'
                    new_path = Path(directory_name)
                    Path.rmdir(new_path)
                except OSError:
                    print('В папке есть файлы')
            elif name == 'видео файлы':
                makedir(pathroot, name)
                for key, value in my_directory_files.items():
                    if key == 'видео файлы':
                        set_of_key = value & new_suffix
                        for elements in set_of_key:
                            for names in files_name:
                                if elements in names:
                                    video_thrade = Thread(target=replace_file, args=(
                                        pathroot, name, names))
                                    video_thrade.start()
                try:

                    directory_name = f'{pathroot}\{name}'
                    new_path = Path(directory_name)
                    Path.rmdir(new_path)
                except OSError:
                    print('В папке есть файлы')
            elif name == 'документы':
                makedir(pathroot, name)
                for key, value in my_directory_files.items():
                    if key == 'документы':
                        set_of_key = value & new_suffix
                        for elements in set_of_key:
                            for names in files_name:
                                if elements in names:
                                    doc_thrade = Thread(target=replace_file, args=(
                                        pathroot, name, names))
                                    doc_thrade.start()
                try:

                    directory_name = f'{pathroot}\{name}'
                    new_path = Path(directory_name)
                    Path.rmdir(new_path)
                except OSError:
                    print('В папке есть файлы')
            elif name == 'музыка':
                makedir(pathroot, name)
                for key, value in my_directory_files.items():
                    if key == 'музыка':
                        set_of_key = value & new_suffix
                        for elements in set_of_key:
                            for names in files_name:
                                if elements in names:
                                    mus_thrade = Thread(target=replace_file, args=(
                                        pathroot, name, names))
                                    mus_thrade.start()
                try:

                    directory_name = f'{pathroot}\{name}'
                    new_path = Path(directory_name)
                    Path.rmdir(new_path)
                except OSError:
                    print('В папке есть файлы')
            elif name == 'архивы':
                makedir(pathroot, name)
                for key, value in my_directory_files.items():
                    if key == 'архивы':
                        set_of_key = value & new_suffix
                        for elements in set_of_key:
                            for names in files_name:
                                if elements in names:
                                    arch_thrade = Thread(target=replace_file_archive, args=(
                                        pathroot, name, names))
                                    arch_thrade.start()

                try:

                    directory_name = f'{pathroot}\{name}'
                    new_path = Path(directory_name)
                    Path.rmdir(new_path)
                except OSError:
                    print('В папке есть файлы')
            elif name == 'неизвестные расширения':
                makedir(pathroot, name)
                for key, value in my_directory_files.items():
                    if key == 'неизвестные расширения':
                        for elements in new_suffix:
                            for names in files_name:
                                if elements in names:
                                    print(f'{elements} это {names}')
                                    other_thrade = Thread(target=replace_file, args=(
                                        pathroot, name, names))
                                    other_thrade.start()
                try:

                    directory_name = f'{pathroot}\{name}'
                    new_path = Path(directory_name)
                    Path.rmdir(new_path)
                except OSError:
                    print('В папке есть файлы')

        end_time = datetime.now()
        dif_time_total = end_time-start_time
        print(f'Затраченое время {dif_time_total.seconds} секунд')


if __name__ == ('__main__'):

    main()
