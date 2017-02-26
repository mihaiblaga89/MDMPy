import cherrypy
from controllers.base import BaseController


class HomeController(BaseController):
    @cherrypy.expose
    def index(self):
        return self.render_template('home/dashboard.html')

    @cherrypy.expose
    def search(self, query=''):
        if not query:
            return {'success' : False}
        else:
            import lib.IGDB as IGDB
            import json
            result = IGDB.Request.get(q=query)
            return json.dumps({'success' : True, 'data' : result})
            # return self.render_template('home/main.html', template_vars={'data' : result})
