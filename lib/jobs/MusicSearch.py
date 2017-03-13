'''
Project : MDMPy2
File : MusicSearch
Author : Lego
Date : 27/02/2017
'''
import models.dbtool as DB
from lib.settings import Settings
import datetime
from lib.Discogs import Request as Discogs
import sys
import pprint
import traceback
from lib.indexers import torznab


def MusicSearch():

    # setting the last run for this task
    Settings.set("music.scheduler.lastrun", datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S.%f"))

    '''
    searching all the songs that are not marked as downloaded
    @TODO search on the enabled indexers types
    '''
    for song in DB.Music.select():
        if not song.downloaded:
            print(song.title)
            try:
                details = Discogs.getId(song.ext_id)
                artistalbum = details['album']['artists'][0]['name'] + ' ' + details['album']['name']
                indexerdata = torznab.Torznab.search(artistalbum)
            except:
                e = sys.exc_info()[0]
                print(pprint.pprint(vars(e)))
