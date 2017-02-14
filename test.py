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
from cptest import BaseCherryPyTestCase

def setUpModule():
    cherrypy.tree.mount(HomeController(), '/')
    cherrypy.engine.start()
setup_module = setUpModule

def tearDownModule():
    cherrypy.engine.exit()
teardown_module = tearDownModule

class TestCherryPyApp(BaseCherryPyTestCase):
    def test_index(self):
        response = self.request('/')
        self.assertEqual(response.output_status, '200 OK')
        # response body is wrapped into a list internally by CherryPy
        self.assertEqual(response.body, ['hello world'])

    def test_echo(self):
        response = self.request('/echo', msg="hey there")
        self.assertEqual(response.output_status, '200 OK')
        self.assertEqual(response.body, ["hey there"])

        response = self.request('/echo', method='POST', msg="back from the future")
        self.assertEqual(response.output_status, '200 OK')
        self.assertEqual(response.body, ["back from the future"])

if __name__ == '__main__':
    import unittest
    unittest.main()