# coding:utf-8

import json
import web
import os
# import inspect

class Controller(object):
    def __init__(self):
        self.__dir = os.path.dirname(os.path.realpath(__file__))
        self.routes = []
        self.input = {}

    def default(self):
        return 'not found'

    def GET(self, path=''):
        if path=='' or path is None:
            return self.default()
        self.input = web.input()
        return self.route(path)
    def POST(self, path=''):
        if path=='' or path is None:
            return self.default()
        self.input = web.input()
        return self.route(path)

    def echo(self, data, code=1000):
        web.header('Content-Type', 'application/json')
        return json.dumps({
            'code': code,
            'data': data
        }, default=str)

    def load(self, path):
        with open(self.__dir+path, 'rb') as f:
            html = f.read()
        return html

    def route(self, path=''):
        # not path.startswith('__') and not path.endswith('__') and 
        if path in self.routes and callable(getattr(self, path)):
            m = getattr(self, path)
            # args = inspect.getargspec(m).args
            # data = web.input()
            return m()
            