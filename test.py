'''
Project : MDMPy2
File : test
Author : Lego
Date : 14/02/2017
'''

# -*- coding: utf-8 -*-
import os.path
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'site-packages')))
import cherrypy

from controllers.home import HomeController
from controllers.settings import SettingsController
from controllers.music import MusicController
from cptest import BaseCherryPyTestCase


def setUpModule():

    cherrypy.site = {
        'base_path': os.getcwd()
    }
    session_dir = cherrypy.site['base_path'] + "/sessions"

    if not os.path.exists(session_dir):
        os.makedirs(session_dir)

    server_config = {
        'tools.sessions.on': True,
        'tools.sessions.storage_type': "file",
        'tools.sessions.storage_path': session_dir,
        'tools.sessions.timeout': 180,

    }

    cherrypy.config.update(server_config)
    cherrypy.tree.mount(HomeController(), '/dashboard')
    cherrypy.tree.mount(SettingsController(), '/settings')
    cherrypy.tree.mount(MusicController(), '/music')
    cherrypy.engine.start()
setup_module = setUpModule


def tearDownModule():
    cherrypy.engine.exit()
teardown_module = tearDownModule


class TestCherryPyApp(BaseCherryPyTestCase):
    def test_index(self):
        response = self.request(path='/dashboard/', app_path='/dashboard')
        self.assertEqual(response.output_status, '200 OK')
        # response body is wrapped into a list internally by CherryPy
        # self.assertEqual(response.body, ['hello world'])

    def test_settings(self):
        response = self.request(path='/settings/', app_path='/settings')
        self.assertEqual(response.output_status, '200 OK')

    def test_music(self):
        response = self.request(path='/music/', app_path='/music')
        self.assertEqual(response.output_status, '200 OK')

    # def test_echo(self):
    #     response = self.request('/echo', msg="hey there")
    #     self.assertEqual(response.output_status, '200 OK')
    #     self.assertEqual(response.body, ["hey there"])
    #
    #     response = self.request('/echo', method='POST', msg="back from the future")
    #     self.assertEqual(response.output_status, '200 OK')
    #     self.assertEqual(response.body, ["back from the future"])

if __name__ == '__main__':
    import unittest
    unittest.main()