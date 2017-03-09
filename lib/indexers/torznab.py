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
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Torznab:

    @staticmethod
    def _request(url):
        try:
            response = requests.get(url)
            tree = ET.fromstring(response.content)
            print(tree)
            for elem in tree.iterfind('channel/item'):
                print(elem.tag)
                print(elem.attrib)
        except requests.RequestException as e:
            print(e.message)

    @staticmethod
    def search(query):

        for indexer in DB.Indexers.select().where(DB.Indexers.type == "torznab"):
            url = indexer.url + '?t=search&extended=1&apikey=' + indexer.api_key + '&limit=100&q=' + urllib.quote_plus(query)
            print('Searching for ' + query + ' in ' + url)
            Torznab._request(url)

