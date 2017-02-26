'''
Project : MDMPy2
File : IGDB
Author : Lego
Date : 14/02/2017
'''

import unirest
from lib.configuration import Cfg
import urllib


class Request():

    @staticmethod
    def get(q=""):
        base_url = "https://igdbcom-internet-game-database-v1.p.mashape.com/games/"
        fields = "?fields=name%2Cfirst_release_date%2Cid%2Ccover&limit=10&offset=0&order=release_dates.date%3Adesc"
        query = "&search=" + urllib.quote(q)

        response = unirest.get(base_url + fields + query,
          headers={
            "X-Mashape-Key": Cfg.get(Cfg(), 'igdb_key'),
            "Accept": "application/json"
          }
        )

        return response.body