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

        # @TODO display the status of the indexers
        indexers = DB.Indexers.select()

        return self.render_template('settings/main.html', template_vars={'jobs' : {}, 'indexers' : indexers})

    @cherrypy.expose
    def shutdown(self):

        cherrypy.engine.exit()

    @cherrypy.expose
    def restart(self):

        cherrypy.engine.restart()

    @classmethod
    @cherrypy.expose
    def addIndexer(cls, type=None, url=None, api_key=None, id=""):

        if not url:
            return json.dumps({"success": False, "error": "url"})
        if not type:
            return json.dumps({"success": False, "error": "type"})
        if type == "torznab" and not api_key:
            return json.dumps({"success": False, "error": "api_key"})

        if id and id != "undefined":
            try:
                update = DB.Indexers.get(DB.Indexers.id == id)
                update.url = url
                update.type = type
                update.api_key = api_key
                update.save()
                return json.dumps({"success": True})
            except:
                return json.dumps({"success": False, "error": "update"})
        else:
            try:
                indexer = DB.Indexers(url=url, type=type, api_key=api_key)
                indexer.save()
                return json.dumps({"success": True})
            except IntegrityError:
                return json.dumps({"success" : False, "error" : "integrity"})

    @classmethod
    @cherrypy.expose
    def removeIndexer(cls, id=None):

        if not id:
            return json.dumps({"success": False, "error": "id"})

        try:
            query = DB.Indexers.delete().where(DB.Indexers.id == id)
            query.execute()
            return json.dumps({"success": True})
        except IntegrityError:
            return json.dumps({"success": False, "error": "integrity"})
