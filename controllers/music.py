'''
Project : MDMPy2
File : settings
Author : Lego
Date : 15/02/2017
'''

import cherrypy
from cherrypy import tools
import json
from controllers.base import BaseController
from peewee import IntegrityError
import sys
import lib.Discogs as Discogs
import models.dbtool as DB


class MusicController(BaseController):

    @staticmethod
    def _parse_args():

        cl = cherrypy.request.headers['Content-Length']
        raw_body = "http://test.com/a?" + cherrypy.request.body.read(int(cl))
        from furl import furl
        return furl(raw_body)

    @cherrypy.expose
    def index(self):

        return self.render_template('music/main.html')

    @cherrypy.expose
    def search(self, query=""):

        result = Discogs.Request.get(q=query)
        return json.dumps({'success': True, 'data': result})

    @cherrypy.expose
    def add(self):

        params = self._parse_args()

        try:
            model = DB.Music(title=params.args['title'], ext_id=params.args['id'], allow_youtube=params.args['allow_youtube'], quality=params.args['quality'], artist=params.args['artist'], album=params.args['album'], album_image=params.args['album_image'])
            model.save()
            return json.dumps({'success' : True})
        except IntegrityError as e:
            print(e)
            return json.dumps({'success' : False})
        except:
            e = sys.exc_info()[0]
            print(e)
            raise

    @cherrypy.expose
    @tools.json_out()
    def yt_search(self):

        from lib.youtube import YouTube
        results = YouTube.search({"q" : 'dimitri vegas', "max_results" : 25})
        return json.dumps(results)