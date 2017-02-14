'''
Project : MDMPy2
File : IGDB
Author : Lego
Date : 14/02/2017
'''

import unirest


class Request():

    base_url = "https://igdbcom-internet-game-database-v1.p.mashape.com/games/"
    fields = "?fields=name%2Cfirst_release_date%2Cid%2Ccover&limit=10&offset=0&order=release_dates.date%3Adesc"
    query = "&search="

    @staticmethod
    def get(q=""):

        response = unirest.get("https://igdbcom-internet-game-database-v1.p.mashape.com/games/?fields=name%2Cfirst_release_date%2Cid%2Ccover&limit=10&offset=0&order=release_dates.date%3Adesc&search=Watchdogs",
          headers={
            "X-Mashape-Key": "kQBXhLiPqimshB5RGtSsZRU1MB9yp1Wfq7XjsnTpqZD7zl6kdc",
            "Accept": "application/json"
          }
        )

        return response.body