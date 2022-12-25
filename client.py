import aiohttp
import asyncio

url = 'http://127.0.0.1:8080/add_lang'


async def post_lang(url):
    async with aiohttp.ClientSession() as session:
        data = {'language': 'Python'}
        post_data = await session.post(url, data=data)
        print(await post_data.text())

asyncio.run(post_lang(url))

