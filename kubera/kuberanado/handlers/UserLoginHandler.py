__author__ = 'hirok_000'

import tornado.web
import ujson

class UserLoginHandler(tornado.web.RequestHandler):


    def post(self):
        print("success")
        test = self.get_argument("test")

        self.write(test)

    def get(self):
        print("get success")
        self.write("get")