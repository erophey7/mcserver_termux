import aiohttp as http
import bs4
import asyncio
import logging

#

async def get(url, sess):
    return

async def main():
    async with http.ClientSession as session:
        tasks = [asyncio.create_task() for i in ]
        asyncio.gather()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)-12s %(asctime)s %(message)s')
    try:
        asyncio.run(main())
    finally:
        logging.info('finished')
