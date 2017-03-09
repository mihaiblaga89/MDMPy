'''
Project : MDMPy2
File : torznab
Author : Lego
Date : 27/02/2017
'''

class Torznab:

    def __init__(self, url=None, port=None ):
        if not url and not port:
            raise Exception("TORZNAB: No port or url provided")
        self.url = url
        self.port = port

    def search(self, query):
        print('Searching for ' + query)