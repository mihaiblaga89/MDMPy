import cherrypy
from controllers.base import BaseController
import lib.IGDB as IGDB


class HomeController(BaseController):
    @cherrypy.expose
    def index(self):
        return self.render_template('home/index.html')

    @cherrypy.expose
    def search(self, query=''):
        if not query:
            return False
        else:
            result = IGDB.Request.get(q="watchdogs")
            print result
            return self.render_template('home/index.html')
