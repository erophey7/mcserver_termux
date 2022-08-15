import aiohttp as http; import bs4; import asyncio; import logging
import pprint
import re
import json as js

async def get(url, sess):
    async with sess.get(url) as resp:
        return await resp.text()


async def request(urls):
    async with http.ClientSession() as session:
        tasks = (asyncio.create_task(get(i, session)) for i in urls)
        return await asyncio.gather(*tasks)


async def vanillaParser() -> tuple:
    _SITE = "https://getbukkit.org/download/vanilla"

    async with http.ClientSession() as session:
        soup = bs4.BeautifulSoup(await get(_SITE, session), 'html.parser')
        download_links = (re.search(r'https://[^"]+', str(i)).group() for i in soup.select('a.btn-download'))
        download_links = (re.search(r'https://[^"]+', str(bs4.BeautifulSoup(i, 'html.parser').select("h2 a"))).group() for i in await request(download_links))
        version_links = (re.search(r'\d\.[^<]+', str(i)).group() for i in soup.select('div.col-sm-3 h2'))

    return tuple(zip(version_links, download_links))


async def forgeParser(version: str='1.17.1'):
    async with http.ClientSession() as session:
        start_page = await get('https://files.minecraftforge.net/net/minecraftforge/forge/index_%s.html' % version, session)
        soup = bs4.BeautifulSoup(start_page, 'html.parser')
        trs = soup.select('tbody tr')
        versions = [re.search(r'\d+\.\d+\.\d+', str(i)).group() for i in trs]
        urls = [f'https://maven.minecraftforge.net/net/minecraftforge/forge/{version}-{i}/forge-{version}-{i}-installer.jar' for i in versions]

        return tuple(zip(versions, urls))


    # {version: [{version: y}, {url: z}]}
    # return (Start_Page)


def vanilla():
    return asyncio.run(vanillaParser())


def forge(version):
    return asyncio.run(forgeParser(version))


# Полигон испытаний

pprint.pprint(forge('1.12.2'))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)-12s %(asctime)s %(message)s')
