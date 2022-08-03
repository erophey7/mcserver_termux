import aiohttp as http
import bs4
import asyncio
import logging
import pprint
import re
import json as js

async def get(url, sess):
    async with sess.get(url) as resp:
        return await resp.text()


async def request(urls):
    async with http.ClientSession() as session:
        tasks = [asyncio.create_task(get(i, session)) for i in urls]
        return await asyncio.gather(*tasks)


async def vanilaParser():
    soup = bs4.BeautifulSoup(str(await request(['https://getbukkit.org/download/vanilla'])), 'html.parser')
    result = str(soup.find_all('div', class_='row vdivide'))
    version = re.findall(r'\d\.\d+\.*\d*', result)[::2]
    gacha_urls = re.findall(r'https://getbukkit.org/get/[^"]*', result)
    soup = bs4.BeautifulSoup(str(await request(gacha_urls)), 'html.parser')
    urls = re.findall(r'https://[^"]*', str(soup.find_all('h2')))

    return list(zip(version, urls))


async def main():
    await vanilaParser()



    # soup = bs4.BeautifulSoup(str(soup.find_all('div', class_='row vdivide')))

    return

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)-12s %(asctime)s %(message)s')

# import aiohttp as http
# import bs4
# import asyncio
# import logging
# import pprint
# import re
# import json as js
#
# class Parser():
#     def __init__(self, server):
#         self.server = server
#         match self.server:
#             case vanila:
#
#     async def get(self, url, sess):
#         async with sess.get(url) as resp:
#             return await resp.text()
#
#     async def request(self, urls):
#         async with http.ClientSession() as session:
#             tasks = [asyncio.create_task(self.get(i, session)) for i in urls]
#             return await asyncio.gather(*tasks)
#
#     async def vanilaParser(self):
#         soup = bs4.BeautifulSoup(str(await self.request(['https://getbukkit.org/download/vanilla'])), 'html.parser')
#         result = str(soup.find_all('div', class_='row vdivide'))
#         version = re.findall(r'\d\.\d+\.*\d*', result)[::2]
#         gacha_urls = re.findall(r'https://getbukkit.org/get/[^"]*', result)
#         soup = bs4.BeautifulSoup(str(await self.request(gacha_urls)), 'html.parser')
#         urls = re.findall(r'https://[^"]*', str(soup.find_all('h2')))
#
#         return list(zip(version, urls))
#
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, format='%(levelname)-12s %(asctime)s %(message)s')