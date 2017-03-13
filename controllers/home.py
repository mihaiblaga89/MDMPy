import cherrypy
from controllers.base import BaseController
import models.dbtool as DB
import lib.IGDB as IGDB
import json


class HomeController(BaseController):

    @cherrypy.expose
    def index(self):

        music = DB.Music.select()
        return self.render_template('home/dashboard.html', template_vars={'music' : music})

    @cherrypy.expose
    def search(self, query=''):

        if not query:
            return {'success' : False}
        else:
            result = IGDB.Request.get(q=query)
            return json.dumps({'success' : True, 'data' : result})
