# coding:utf-8

import json
import web
import config

class Model(object):
    def __init__(self):
        # self.__tbn = None
        self.dbn = None
        self.db = None
        
    def initdb(self):
        """
            init db with dbn[mysql], db(database name), user, password
        """
        if self.db is None and self.dbn is not None:
            self.db = web.database(dbn=config.db['dbn'], db=self.dbn, user=config.db['user'], pw=config.db['pw'])