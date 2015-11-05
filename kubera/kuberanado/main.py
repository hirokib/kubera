__author__ = 'hirok_000'


import tornado.ioloop
import tornado.web
import databaseConnector
from handlers.UserLoginHandler import UserLoginHandler
from handlers.mainHandler import MainHandler

class Application(tornado.web.Application):

    def __init__(self):
        
        self.db = databaseConnector.DatabaseConnector('customers.db')

        handlers = [
        (r"/user", UserLoginHandler),
        (r"/", MainHandler),
        ]

        tornado.web.Application.__init__(self, handlers, autoreload=True)



def main():
    http_server = Application()
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()



