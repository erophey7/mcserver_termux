# some imports
import requests
import json
import bs4
import re
import os

CURDIR = os.path.dirname(__file__)

class Java(object):

    def __init__(self):
        super().__init__()
        self.versions = []

    def updateVersions(self):
        with open("{}/data/java/versions.json".format(CURDIR)) as f:
            versions = json.load(f)


    @property
    def DownloadsLinks(self, version: str = None):

        with open("{}/data/java/Links.json".format(CURDIR), "w+") as f:

            if f.read() == '':
                f.write("{}")
                return 0 # TODO: <- Call update method

            jsonJava = json.load(f)

            if version is None:
                return 1 # TODO: <- Call versions update method



if __name__ == '__main__':
    print(Java().DownloadsLinks)
