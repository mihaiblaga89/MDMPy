'''
Project : MDMPy2
File : settings
Author : Lego
Date : 15/02/2017
'''

import cherrypy
from controllers.base import BaseController


class SettingsController(BaseController):
    @cherrypy.expose
    def index(self):
        return self.render_template('settings/main.html')

    @cherrypy.expose
    def shutdown(self):
        import cherrypy
        # cherrypy.engine.stop()
        cherrypy.engine.exit()

    @cherrypy.expose
    def restart(self):
        import cherrypy
        cherrypy.engine.restart()
