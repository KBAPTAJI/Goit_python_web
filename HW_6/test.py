from asyncio import futures
import asyncio
import aiohttp


async def make_requests(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print('Status :', response.status)
            html = await response.text()
    return html

futures = [make_requests('http://www.google.com.ua')]

results = asyncio.run(*futures)
print(results)
