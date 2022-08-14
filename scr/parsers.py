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

async def vanillaParser():
    SITE = "https://getbukkit.org/download/vanilla"
    async with http.ClientSession() as session:
        soup = bs4.BeautifulSoup(await get(SITE, session), 'html.parser')
        download_links = [re.search(r'https://[^"]+', str(i)).group() for i in soup.select('a.btn-download')]

        version_links = [re.search(r'\d\.[^<]+', str(i)).group() for i in soup.select('div.col-sm-3 h2')]
        return list(zip(version_links, download_links))

# Vanilla minecraft site parser

# async def vanillaParser():
#     soup = bs4.BeautifulSoup(str(await request(['https://getbukkit.org/download/vanilla'])), 'html.parser')
#     result = str(soup.find_all('div', class_='row vdivide'))
#     version = re.findall(r'\d\.\d+\.*\d*', result)[::2]
#     gacha_urls = re.findall(r'https://getbukkit.org/get/[^"]*', result)
#     soup = bs4.BeautifulSoup(str(await request(gacha_urls)), 'html.parser')
#     urls = re.findall(r'https://[^"]*', str(soup.find_all('h2')))
#
#     return list(zip(version, urls))


def vanilla():
    return asyncio.run(vanillaParser())

# Полигон испытаний

pprint.pprint(vanilla())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)-12s %(asctime)s %(message)s')
