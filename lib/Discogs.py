'''
Project : MDMPy2
File : IGDB
Author : Lego
Date : 14/02/2017
'''

import requests
import urllib
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# disable urllib ssl warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# TODO make a better version of this
class Request():

    @staticmethod
    def request(params="", json=True):

        base_url = "https://api.spotify.com/v1/"
        url = base_url + params
        response = requests.get(url, verify=False)
        if json:
            return response.json()
        else:
            return response

    @staticmethod
    def get(q=""):

        if not q:
            raise Exception('No query provided')

        return Request.request("search?q=" + urllib.quote_plus(q) + "&type=track")

    @staticmethod
    def getId(id=""):

        if not id:
            raise Exception('No ID provided')
        return json.loads(Request.request('tracks/' + id, json=False).text)

