import asyncio
from pathlib import Path
from aiopath import AsyncPath
from asynctempfile import NamedTemporaryFile
from time import time
import sys
import os
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


async def walk_folders(pathroot):
    for name_file in pathroot.iterdir():
        if name_file.is_file():
            for name, value in my_directory_files.items():
                if name == 'изображения' and str(name_file.suffix).casefold() in str(value).casefold():
                    await makedir(pathroot, name)
                    await replace_file(pathroot, name, name_file.name)
                elif name == 'видео файлы' and str(name_file.suffix).casefold() in str(value).casefold():
                    await makedir(pathroot, name)
                    await replace_file(pathroot, name, name_file.name)
                elif name == 'документы' and str(name_file.suffix).casefold() in str(value).casefold():
                    await makedir(pathroot, name)
                    await replace_file(pathroot, name, name_file.name)
                elif name == 'видео файлы' and str(name_file.suffix).casefold() in str(value).casefold():
                    await makedir(pathroot, name)
                    await replace_file(pathroot, name, name_file.name)
                elif name == 'архивы' and str(name_file.suffix).casefold() in str(value).casefold():
                    await makedir(pathroot, name)
                    await replace_file(pathroot, name, name_file.name)
                    unpackarchive(pathroot, name, name_file)
                elif name == 'неизвестные расширения':
                    await makedir(pathroot, 'неизвестные расширения')
                    await replace_file(pathroot, name, name_file.name)
        else:
            await walk_folders(name_file)


async def replace_file(pathroot, name, filename):
    try:
        initpath = AsyncPath(f'{pathroot}/{filename}')
        new_path = f'{pathroot}/{name}/{filename}'
        await initpath.replace(new_path)
    except WindowsError:
        print('файл не найден')


async def makedir(pathroot, name):
    new_path = AsyncPath(f'{pathroot}/{name}')
    try:
        await new_path.mkdir()
    except FileExistsError:
        print('Папка уже существует, создавать не надо')


def replace_file_archive(pathroot, name, filename):
    try:
        directory_name = f'{pathroot}\{name}'
        new_path = Path(directory_name)
        os.replace(f'{pathroot}\{filename}',
                   f'{new_path}\{normalize(filename)}')
    except WindowsError:
        print('файл не найден')


def unpackarchive(pathroot, name, namefile):
    shutil.unpack_archive(
        f'{pathroot}\{name}\{namefile}', f'{pathroot}\{name}')


async def main():
    if len(sys.argv) < 2:
        print('аргументов меньше 1')
    else:
        start_time = time()
        pathroot_2 = sys.argv[1]
        pathroot = Path(pathroot_2)
        if pathroot.exists():
            if pathroot.is_dir():
                future = walk_folders(pathroot)
                await asyncio.gather(future)
        end_time = time()
        dif_time_total = end_time-start_time
        print(f'Затраченое время {dif_time_total} секунд')


if __name__ == ('__main__'):
    asyncio.run(main())
