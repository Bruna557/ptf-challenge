import swagger_ui
import tornado.ioloop
import tornado.web
import tornado.httpserver

from api import users_controller
from persistence import user_repository, cache
import settings


def make_app():
    handlers = [
        (r'/api/users/?(.*)?', users_controller.UsersController,
         dict(repository = user_repository.UserRepository(), cache = cache.RedisDb()))
    ]
    app = tornado.web.Application(handlers)

    swagger_ui.api_doc(
        app,
        config_path='./doc/swagger.json',
        url_prefix='/swagger/spec.html',
        title='Power to Fly - BE Challenge',
    )

    return app


if __name__ == '__main__':
    app = make_app()
    app.listen(settings.APP_PORT)
    tornado.ioloop.IOLoop.current().start()
