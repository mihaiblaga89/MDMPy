'''
Project : MDMPy2
File : settings
Author : Lego
Date : 15/02/2017
'''

import cherrypy
from controllers.base import BaseController
import models.dbtool as DB
from peewee import IntegrityError
import json


class SettingsController(BaseController):

    @cherrypy.expose
    def index(self):

        #@TODO display the status of the indexers
        indexers = DB.Indexers.select()

        return self.render_template('settings/main.html', template_vars={'jobs' : {}, 'indexers' : indexers})

    @cherrypy.expose
    def shutdown(self):

        cherrypy.engine.exit()

    @cherrypy.expose
    def restart(self):

        cherrypy.engine.restart()

    @cherrypy.expose
    def addIndexer(self, type=None, url=None, api_key=None):

        if not url:
            return json.dumps({"success": False, "error": "url"})
        if not type:
            return json.dumps({"success": False, "error": "type"})
        if type == "torznab" and not api_key:
            return json.dumps({"success": False, "error": "api_key"})
        try:
            indexer = DB.Indexers(url=url, type=type, api_key=api_key)
            indexer.save()
            return json.dumps({"success": True})
        except IntegrityError:
            return json.dumps({"success" : False, "error" : "integrity"})

    @cherrypy.expose
    def removeIndexer(self, url=None):

        if not url:
            return json.dumps({"success": False, "error": "url"})

        try:
            query = DB.Indexers.delete().where(DB.Indexers.url == url)
            query.execute()
            return json.dumps({"success": True})
        except IntegrityError:
            return json.dumps({"success": False, "error": "integrity"})
