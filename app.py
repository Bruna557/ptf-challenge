import swagger_ui
import tornado.ioloop
import tornado.web
import tornado.httpserver

from api import users_controller
from models.user import User
from persistence import db, cache, user_repository
from settings import APP_SETTINGS


def make_app():
    session = db.get_session(APP_SETTINGS['db_connection_string'])
    repository = user_repository.UserRepository(entity=User, session=session)
    redis = cache.RedisDb(APP_SETTINGS['cache_host'],
                          APP_SETTINGS['cache_port'],
                          APP_SETTINGS['cache_pwd'],
                          APP_SETTINGS['cache_expiration'])

    handlers = [
        (r'/api/users/?(.*)?', users_controller.UsersController, dict(repository=repository, cache=redis))
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
    app.listen(APP_SETTINGS['app_port'])
    tornado.ioloop.IOLoop.current().start()
