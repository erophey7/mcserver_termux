# Some libraries
import pprint

import requests
import logging
import json
import bs4
import re
import os

# import ujson as json

# Constants мда...
DIRPATH = os.path.dirname(__file__)

VANILLA = "https://getbukkit.org/download/vanilla"
FORGE = "https://files.minecraftforge.net/net/minecraftforge/forge/index_%s.html"
SPIGOT = "https://getbukkit.org/download/spigot"


def vanilla(version: str = None):
    with requests.Session() as session:

        with open("{}/data/vanilla.json".format(DIRPATH), "r") as f:
            vanilla = json.load(f)

        html = session.get(VANILLA).text
        soup = bs4.BeautifulSoup(html, "html.parser")

        versions = [str(i)[4:-5] for i in soup.select("div > h2")]

        if version is None:
            return versions

        elif versions[0] in vanilla:
            return vanilla[version]

        elif version not in versions:
            return False

        tempDownloadsLinks = [
            re.search(r'https://[^"]+', str(i)).group()
            for i in soup.select("a.btn-download")
        ]

        downloadLinks = []

        for j, i in enumerate(tempDownloadsLinks):
            downloadLinks.append(
                re.search(
                    r'https://[^"]+',
                    str(
                        bs4.BeautifulSoup(
                            session.get(tempDownloadsLinks[j]).text, "html.parser"
                        ).select("h2 a")
                    ),
                ).group()
            )

        dumpsLinks = {versions[i]: downloadLinks[i] for i in range(len(versions))}

        with open("{}/data/vanilla.json".format(DIRPATH), "w") as f:
            json.dump(dumpsLinks, f)

        return dumpsLinks[version]


#
# def vanilla.json() -> tuple:
#
#     soup = bs4.BeautifulSoup(requests.request("get", VANILLA).text, "html.parser")
#     download_links = (
#     re.search(r'https://[^"]+', str(i)).group()
#             for i in soup.select("a.btn-download")
#         )
#         download_links = (
#             re.search(
#                 r'https://[^"]+',
#                 str(bs4.BeautifulSoup(i, "html.parser").select("h2 a")),
#             ).group()
#             for i in await request(download_links)
#         )
#         version_links = (
#             re.search(r"\d\.[^<]+", str(i)).group()
#             for i in soup.select("div.col-sm-3 h2")
#         )
#
#     return tuple(zip(version_links, download_links))
#
#
# async def _forgeParser(version: str):
#     async with http.ClientSession() as session:
#         Start_Page = await get(
#             "https://files.minecraftforge.net/net/minecraftforge/forge/index_%s.html"
#             % version,
#             session,
#         )
#         soup = bs4.BeautifulSoup(Start_Page, "html.parser")
#         trs = soup.select("tbody tr")
#         versions = [re.search(r"\d+\.\d+\.\d+", str(i)).group() for i in trs]
#         urls = [
#             f"https://maven.minecraftforge.net/net/minecraftforge/forge/{version}-{i}/forge-{version}-{i}-installer.jar"
#             for i in versions
#         ]
#
#         return tuple(zip(versions, urls))
#
#
# async def _spigotParser(version):
#     _SITE =
#
#     async with http.ClientSession() as session:
#         soup = bs4.BeautifulSoup(await get(_SITE, session), "html.parser")
#         download_links = (
#             re.search(r'https://[^"]+', str(i)).group()
#             for i in soup.select("a.btn-download")
#         )
#         download_links = (
#             re.search(
#                 r'https://[^"]+',
#                 str(bs4.BeautifulSoup(i, "html.parser").select("h2 a")),
#             ).group()
#             for i in await request(download_links)
#         )
#         versions = (
#             re.search(r"\d\.[^<]+", str(i)).group()
#             for i in soup.select("div.col-sm-3 h2")
#         )
#         result = dict(zip(versions, download_links))
#
#     return result[version]
#
#     # {version: [{version: y}, {url: z}]}
#     # return (Start_Page)
#
#
# def vanilla.json():
#     return asyncio.run(_vanillaParser())
#
#
# def forge(version):
#     return asyncio.run(_forgeParser(version))
#
#
# def spigot(version):
#     return asyncio.run(_spigotParser(version))
#
#
# # Полигон испытаний
#
# pprint.pprint(spigot("1.12.2"))

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)-12s %(asctime)s %(message)s"
    )
    vanilla()
