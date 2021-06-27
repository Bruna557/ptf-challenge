import functools
from http import HTTPStatus
import json
from logzero import logger

from .controller import Controller
from exception.enitity_not_found import EntityNotFound
from persistence.cache import RedisDb


class UsersController(Controller):
    def initialize(self, repository):
        self.repository = repository
        self.cache = RedisDb()

    # pylint: disable=no-method-argument
    def handle():
        def decorator(function):
            @functools.wraps(function)
            def wrapper(self, *args):
                try:
                    result = function(self, *args)
                    self.write_response(status_code=HTTPStatus.OK,result=result)
                except EntityNotFound:
                    logger.error('Entity not found')
                    self.write_error(status_code=HTTPStatus.NOT_FOUND,
                                        message='entity not found')
                except Exception as err:
                    logger.error(str(err))
                    self.write_error(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                        message=str(err))
            return wrapper
        return decorator

    @handle()
    def get(self, key):
        if not key:
            offset, limit = self._get_pagination()
            filter = self._get_filter()
            cache_key = f'offset:{offset},limit:{limit}' + json.dumps(filter)
            result = self.cache.get_data(cache_key)
            if result:
                return result
            result = self._to_json(self.repository.get_all(offset, limit, **filter))
            self.cache.set_data(cache_key, result)
            return result
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
        page_size = int(self.get_argument('page_size', 20, True))
        page_number = int(self.get_argument('page_number', 1, True))
        return page_size*(page_number-1), page_size

    def _to_json(self, result):
        try:
            if type(result) is list:
                serializable_result = [row.to_dict() for row in result]
            else:
                serializable_result = result.to_dict()
            return json.dumps(serializable_result)
        except:
            return json.dumps(result)