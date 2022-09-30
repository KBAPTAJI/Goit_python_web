import asyncio
from pathlib import Path
from aiopath import AsyncPath

pathroot = ['C:/Python/rr/test.txt', ]


async def makedir(pathroot):
    path = Path(f'{pathroot}')
    apath = AsyncPath(path)
    print(path)
    print(apath)
    await apath.replace('C:/Python/rr/new/test.txt')


async def main():

    futur = [makedir(i) for i in pathroot]
    await asyncio.gather(*futur)


if __name__ == '__main__':
    asyncio.run(main())
