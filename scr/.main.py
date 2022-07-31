import aiohttp as http
import bs4
import asyncio
import logging
import pprint
import re

URLS = ['https://getbukkit.org/download/vanilla']

async def get(url, sess):
    async with sess.get(url) as resp:
        return await resp.text()


async def request(urls):
    async with http.ClientSession() as session:
        tasks = [asyncio.create_task(get(i, session)) for i in urls]
        return await asyncio.gather(*tasks)


async def main():
    soup = bs4.BeautifulSoup(str(await request(URLS)),'html.parser')
    result = str(soup.find_all('div', class_='row vdivide'))
    version = re.findall(r'\d\.\d+\.\d', result)
    gacha_urls = re.findall(r'https://getbukkit.org/get/[^"]*', result)
    soup = bs4.BeautifulSoup(str(await request(gacha_urls)),'html.parser')
    urls = re.findall( r'https://[^"]*',str(soup.find_all('h2')))
    pprint.pprint(soup)
    # urls = re.findall(r'https://\.jar')
    # pprint.pprint(urls)


    # soup = bs4.BeautifulSoup(str(soup.find_all('div', class_='row vdivide')))

    return

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)-12s %(asctime)s %(message)s')
    try:
        asyncio.run(main())
    finally:
        logging.info('finished')
