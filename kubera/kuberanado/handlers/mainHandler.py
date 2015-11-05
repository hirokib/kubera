__author__ = 'hirok_000'

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.Application.db.delete()
        self.write("Hello, dgasdrld")
