'''
Project : MDMPy2
File : IGDB
Author : Lego
Date : 14/02/2017
'''

import requests
from lib.configuration import Cfg
import urllib


class Request():

    @staticmethod
    def get(q=""):
        base_url = "https://api.spotify.com/v1/"
        fields = "&type=track"
        query = "search?q=" + urllib.quote_plus(q)

        url = base_url + query + fields
        response = requests.get(url, verify=False)

        return response.json()