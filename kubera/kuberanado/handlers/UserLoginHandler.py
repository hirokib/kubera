__author__ = 'hirok_000'

import tornado.web
import ujson

class UserLoginHandler(tornado.web.RequestHandler):

    def post(self):
        print("success")
        db = self.application.db
        test = self.get_argument("test")
        result = db.execute("SELECT * FROM USERS")
        self.write(ujson.dumps(result))

    def get(self):
        print("get success")
        self.write("get")