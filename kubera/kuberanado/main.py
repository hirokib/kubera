__author__ = 'hirok_000'


import tornado.ioloop
import tornado.web
from handlers.UserLoginHandler import UserLoginHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, dgasdrld")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/user", UserLoginHandler),
        (r"/", MainHandler),

    ], autoreload=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()