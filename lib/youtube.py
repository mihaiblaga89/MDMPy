'''
Project : MDMPy2
File : youtube
Author : Lego
Date : 26/02/2017
'''
import sys
import os.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../site-packages')))

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pprint
from lib.configuration import Cfg

YOUTUBE_API_VERSION = "v3"


class YouTube():

    @staticmethod
    def _search(options):
        yt = build("youtube", YOUTUBE_API_VERSION, developerKey=Cfg.get(Cfg(), 'youtube_api_key'))

        # Call the search.list method to retrieve results matching the specified
        # query term.
        search_response = yt.search().list(
            q=options['q'],
            part="id,snippet",
            maxResults=options['max_results']
        ).execute()

        videos = []

        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append(search_result)

        return videos

    @staticmethod
    def search(options):
        try:
            return YouTube._search(options)
        except HttpError, e:
            print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
            return {"success" : False}


# if __name__ == "__main__":
#   argparser.add_argument("--q", help="Search term", default="Google")
#   argparser.add_argument("--max-results", help="Max results", default=25)
#   args = argparser.parse_args()
#
#   try:
#     YouTube.search(args)
#   except HttpError, e:
#     print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)