import swagger_ui
import tornado.ioloop
from tornado.options import options
import tornado.web
import tornado.httpserver

from api import users_controller
from models.user import User
from persistence import db, cache, user_repository
from settings import APP_SETTINGS


def make_app(provided_cache=None, test=False):
    session, engine = db.get_session(APP_SETTINGS['db_connection_string'])
    repository = user_repository.UserRepository(entity=User, session=session)
    _cache = provided_cache or cache.RedisDb(APP_SETTINGS['cache_host'],
                                             APP_SETTINGS['cache_port'],
                                             APP_SETTINGS['cache_pwd'],
                                             APP_SETTINGS['cache_expiration'])

    handlers = [
        (r'/api/users/?(.*)?', users_controller.UsersController, dict(repository=repository, cache=_cache))
    ]
    app = tornado.web.Application(handlers)

    swagger_ui.api_doc(
        app,
        config_path='./doc/swagger.json',
        url_prefix='/swagger/spec.html',
        title='Power to Fly - BE Challenge',
    )

    if test:
        db.create_db(engine)

    return app


if __name__ == '__main__':
    app = make_app()
    tornado.options.parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
