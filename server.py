import tornado.ioloop
import tornado.web
import tornado.httpserver

from handlers import users_handler
from repositories import user_repository
from config import load_config
from database import db # remove


config = load_config()

def make_app():
    return tornado.web.Application([
        (r'/api/users/?(.*)?',users_handler.UsersHandler,dict(repository=user_repository.UserRepository()))
    ])


def runserver():
    try:
        print("Starting server...")
        db.clean_db()
        http_server = tornado.httpserver.HTTPServer(make_app())
        http_server.listen(config["port"])
        print("Listening on port:", config["port"])
        print("Database url:", config["database_url"])
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
        print("Server shut down, exiting...")


if __name__ == "__main__":
    runserver()