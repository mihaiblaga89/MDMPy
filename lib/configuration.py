'''
Project : MDMPy2
File : config
Author : Lego
Date : 16/02/2017
'''

from config import Config
import os

class Cfg():

    def __init__(self):
        self.cfg = Config(file('config.cfg'))

    def get(self, string=''):
        return self.cfg[string]