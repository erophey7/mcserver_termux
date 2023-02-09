# Some libraries
import requests
import json
import bs4
import re
import os

# Constants
DIRPATH = os.path.dirname(__file__)

VANILLA = "https://getbukkit.org/download/vanilla"
FORGE = "https://files.minecraftforge.net/net/minecraftforge/forge/"
SPIGOT = "https://getbukkit.org/download/spigot"

# Vanilla


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


# Forge

def forge(version: str = None):

    with requests.Session() as session:

        with open("{}/data/forge.json".format(DIRPATH), "r") as f:
            forge = json.load(f)

        html = session.get(FORGE).text
        soup = bs4.BeautifulSoup(html, "html.parser")
        versions = [
            re.search(r"\d+(\.\d+)+", str(i)).group()
            for i in soup.select("li > ul > li")
        ]

        if version is None:
            return versions
        if version in forge:
            return forge[version].split('url=')[1]
        if version not in versions:
            return None

        tempDownloadLinks = [
            bs4.BeautifulSoup(
                session.get(
                    "https://files.minecraftforge.net/net/minecraftforge/forge/index_{}.html".format(i)
                ).text,
                "html.parser",
            ).select("div.link-boosted > a")
            for i in versions
        ]

        downloadLinks = {
            versions[j]:
                re.search(r'href="[^"]+',str(tempDownloadLinks[j][0])).group()[6:]
            if tempDownloadLinks[j] != [] else None
            for j, i in enumerate(versions)
        }

        with open("{}/data/forge.json".format(DIRPATH), "w") as f:
            json.dump(downloadLinks, f)

        return downloadLinks[version].split('url=')[1]


# Spigot

def spigot(version: str = None):
    with requests.Session() as session:

        with open("{}/data/spigot.json".format(DIRPATH)) as f:
            spigot = json.load(f)

        html = session.get(SPIGOT).text
        soup = bs4.BeautifulSoup(html, "html.parser")

        versions = [str(i)[4:-5] for i in soup.select("div > h2")]

        if version is None:
            return versions

        elif versions[0] in spigot:
            return spigot[version]

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

        with open("{}/data/spigot.json".format(DIRPATH), "w") as f:
            json.dump(dumpsLinks, f)

        return dumpsLinks[version].split('url=')[1]

    # {version: [{version: y}, {url: z}]}
    # return (Start_Page)


# Полигон испытаний

if __name__ == "__main__":
    print(forge('1.12.2'))
