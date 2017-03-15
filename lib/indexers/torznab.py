'''
Project : MDMPy2
File : torznab
Author : Lego
Date : 27/02/2017
'''
import models.dbtool as DB
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib
import sys
import os.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../site-packages')))
import xmltodict
from pprint import pprint

# Disable urllib3 ssl warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Torznab:

    @staticmethod
    def _request(url):

        try:
            response = requests.get(url)
            tree = xmltodict.parse(response)
            pprint(tree)

        except requests.RequestException as e:
            print(e.message)

    @staticmethod
    def search(query):

        for indexer in DB.Indexers.select().where(DB.Indexers.type == "torznab"):
            url = indexer.url + '?t=search&extended=1&apikey=' + indexer.api_key + '&limit=100&q=' + urllib.quote_plus(query)
            print('Searching for ' + query + ' in ' + url)
            Torznab._request(url)

