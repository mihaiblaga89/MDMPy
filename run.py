import sys
import os.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'site-packages')))
import cherrypy
import os
from controllers.home import *
from controllers.settings import *
from controllers.music import *
from site_config import SiteConfig
from models.loghelper import Logger
from models.dbtool import *
from lib.jobs.MusicSearch import *
from controllers.auth import require, member_of, name_is


cherrypy.engine.housekeeper = cherrypy.process.plugins.BackgroundTask(60, MusicSearch)
cherrypy.engine.housekeeper.start()


def removeDb():
    if os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), 'mdmpy.db'))):
        os.remove(os.path.abspath(os.path.join(os.path.dirname(__file__), 'mdmpy.db')))
        print("DB removed");

# removeDb()
initializeDatabase()

# this method returns HTML when a 404 (page not found error) is encountered.
# You'll probably want to return custom HTML using Jinja2.
def error_page_404(status, message, traceback, version):
    a = cherrypy.request
    b = cherrypy.url()
    return "404 Error! How the heck did you got here?"


# this returns an HTML error message when an exception is thrown in your code in production.
# This to avoid showing a stack trace with sensitive information.
def handle_error():
    cherrypy.response.status = 500
    cherrypy.response.body = [
        "<html><body>Oh crap...I have failed you master</body></html>".encode()
    ]


class RootController:
    @cherrypy.expose
    def index(self, *args, **kwargs):
        c = HomeController()
        return c.index()


def start_server():
    cherrypy.site = {
        'base_path': os.getcwd()
    }

    # make sure the directory for storing session files exists
    session_dir = cherrypy.site['base_path'] + "/sessions"

    if not os.path.exists(session_dir):
        os.makedirs(session_dir)

    # this is where I initialize a custom tool for connecting to the database, once for each
    # request. Edit models/dbtool.py and uncomment the tools.db lines below to use this.
    # cherrypy.tools.db = DbTool()

    server_config = {
        # This tells CherryPy what host and port to run the site on (e.g. localhost:3005/)
        # Feel free to set this to whatever you'd like.
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 3005,

        'error_page.404': error_page_404,
        'engine.autoreload.on': True,

        # this indicates that we want file-based sessions (not stored in RAM, which is the default)
        # the advantage of this is that you can stop/start CherryPy and your sessions will continue
        'tools.sessions.on': True,
        'tools.sessions.storage_type': "file",
        'tools.sessions.storage_path': session_dir,
        'tools.sessions.timeout': 180,

        # this is a custom tool for handling authorization (see auth.py)
        'tools.auth.on': True,
        'tools.auth.priority': 52,
        'tools.sessions.locking': 'early'

        # uncomment the below line to use the tool written to connect to the database
        # 'tools.db.on': True
    }

    if SiteConfig.is_prod:
        server_config['request.error_response'] = handle_error

    cherrypy.config.update(server_config)

    # this will let us access localhost:3005/Home or localhost:3005/Home/Index
    cherrypy.tree.mount(HomeController(), '/dashboard')
    cherrypy.tree.mount(SettingsController(), '/settings')
    cherrypy.tree.mount(MusicController(), '/music')

    # this will map localhost:3005/
    cherrypy.tree.mount(RootController(), '/', {
        '/': {
            'tools.staticdir.root': os.getcwd()
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static',

            # we don't need to initialize the database for static files served by CherryPy
            # 'tools.db.on': False
        }
    })

    cherrypy.engine.start()
    cherrypy.engine.block()

    # this return value is used by the WSGI server in prod
    return cherrypy.tree


try:
    application = start_server()
except Exception as ex:
    Logger.error('Error during run', ex)
