import functools
from http import HTTPStatus
import json
from logzero import logger

from .controller import Controller
from exception.enitity_not_found import EntityNotFound


class UsersController(Controller):
    def initialize(self, repository, cache):
        self.repository = repository
        self.cache = cache

    # pylint: disable=no-method-argument
    def handle():
        def decorator(function):
            @functools.wraps(function)
            def wrapper(self, *args):
                try:
                    result = function(self, *args)
                    self.write_response(status_code=HTTPStatus.OK,result=result)
                except EntityNotFound:
                    logger.error('User not found')
                    self.write_error(status_code=HTTPStatus.NOT_FOUND,
                                     message='User not found')
                except Exception as err:
                    logger.error(str(err))
                    self.write_error(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                     message=str(err))
            return wrapper
        return decorator

    @handle()
    def get(self, key):
        if not key:
            page_size, current_page = self._get_pagination()
            filter = self._get_filter()
            cache_key = f'page_size:{page_size},current_page:{current_page}' + json.dumps(filter)
            if cached_result := self.cache.get_data(cache_key):
                result = json.loads(cached_result)
                cache_hit = True
            else:
                result = self.repository.get_all(page_size*(current_page-1), page_size, **filter)
                self.cache.set_data(cache_key, json.dumps(result))
                cache_hit = False
            return {'data': result['data'],
                    'page_size': page_size,
                    'current_page': current_page,
                    'next_page': result['next_page'],
                    'cache': cache_hit}
        else:
            return self.repository.get_by_id(key)

    @handle()
    def post(self, key):
        return self.repository.save(json.loads(self.request.body))

    def _get_filter(self):
        filter = {}
        if first_name := self.get_argument('first_name', None, True):
            filter['first_name'] = first_name
        if last_name := self.get_argument('last_name', None, True):
            filter['last_name'] = last_name
        if email := self.get_argument('email', None, True):
            filter['email'] = email
        return filter

    def _get_pagination(self):
        return int(self.get_argument('page_size', 20, True)), int(self.get_argument('current_page', 1, True))
