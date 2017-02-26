'''
Project : MDMPy2
File : settings
Author : Lego
Date : 15/02/2017
'''

import cherrypy
import json
from controllers.base import BaseController
from peewee import IntegrityError
import sys


class MusicController(BaseController):
    @cherrypy.expose
    def index(self):
        return self.render_template('music/main.html')

    @cherrypy.expose
    def search(self, query=""):
        import lib.Discogs as Discogs
        result = Discogs.Request.get(q=query)
        return json.dumps({'success': True, 'data': result})

    @cherrypy.expose
    def add(self):
        import models.dbtool as DB
        cl = cherrypy.request.headers['Content-Length']
        rawbody = "http://test.com/a?" + cherrypy.request.body.read(int(cl))
        from furl import furl
        f = furl(rawbody)
        print f.args['title']

        try:
            model = DB.Music(title=f.args['title'], ext_id=f.args['id'], allow_youtube=f.args['allow_youtube'], quality=f.args['quality'], artist=f.args['artist'], album=f.args['album'])
            model.save()
            return json.dumps({'success' : True})
        except IntegrityError as e:
            print(e)
            return json.dumps({'success' : False})
        except:
            e = sys.exc_info()[0]
            print(e)
            raise
            return json.dumps({'success': False})