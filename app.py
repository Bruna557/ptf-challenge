import tornado.ioloop
import tornado.web
import tornado.httpserver

from api import users_controller
from repositories import user_repository


def make_app():
    return tornado.web.Application([
        (r'/api/users/?(.*)?',users_controller.UsersController,dict(repository=user_repository.UserRepository()))
    ])


def runserver():
    try:
        print('Starting server...')
        http_server = tornado.httpserver.HTTPServer(make_app())
        http_server.listen('8080')
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
        print('Server shut down, exiting...')


if __name__ == '__main__':
    runserver()