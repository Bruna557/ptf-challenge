import json
from random import randint
from tornado.testing import AsyncHTTPTestCase

from app import make_app
from .fixtures import CacheFixture
from models.user import User
from persistence import db


class TestUserController(AsyncHTTPTestCase):
    def get_app(self):
        cache = CacheFixture()
        return make_app(provided_cache=cache,test=True)

    def test_get_should_return_no_users(self):
        response = self.fetch('/api/users', method='GET')
        response_body = json.loads(response.body)

        self.assertEqual(200, response.code)
        self.assertEqual(0, len(response_body['data']))
        self.assertEqual(20, response_body['page_size'])
        self.assertEqual(1, response_body['current_page'])
        self.assertFalse(response_body['next_page'])
        self.assertFalse(response_body['cache'])

    def test_get_should_return_users(self):
        self._insert_users()

        response = self.fetch('/api/users?page_size=2&current_page=1', method='GET')
        response_body = json.loads(response.body)

        self.assertEqual(200, response.code)
        self.assertEqual(2, len(response_body['data']))
        self.assertEqual(2, response_body['page_size'])
        self.assertEqual(1, response_body['current_page'])
        self.assertTrue(response_body['next_page'])
        self.assertFalse(response_body['cache'])

        response = self.fetch('/api/users?page_size=2&current_page=2', method='GET')
        response_body = json.loads(response.body)

        self.assertEqual(200, response.code)
        self.assertEqual(1, len(response_body['data']))
        self.assertEqual(2, response_body['page_size'])
        self.assertEqual(2, response_body['current_page'])
        self.assertFalse(response_body['next_page'])
        self.assertFalse(response_body['cache'])

    def test_get_should_filter_users(self):
        self._insert_users()

        response = self.fetch('/api/users?page_size=5&current_page=1&first_name=anna', method='GET')
        response_body = json.loads(response.body)

        self.assertEqual(200, response.code)
        self.assertEqual(2, len(response_body['data']))
        self.assertEqual(5, response_body['page_size'])
        self.assertEqual(1, response_body['current_page'])
        self.assertFalse(response_body['next_page'])
        self.assertFalse(response_body['cache'])

    def test_get_should_cache(self):
        self._insert_users()

        response = self.fetch('/api/users', method='GET')
        response_body = json.loads(response.body)

        self.assertEqual(200, response.code)
        self.assertEqual(3, len(response_body['data']))
        self.assertEqual(20, response_body['page_size'])
        self.assertEqual(1, response_body['current_page'])
        self.assertFalse(response_body['next_page'])
        self.assertFalse(response_body['cache'])

        response = self.fetch('/api/users', method='GET')
        response_body = json.loads(response.body)

        self.assertEqual(200, response.code)
        self.assertEqual(3, len(response_body['data']))
        self.assertEqual(20, response_body['page_size'])
        self.assertEqual(1, response_body['current_page'])
        self.assertFalse(response_body['next_page'])
        self.assertTrue(response_body['cache'])

    def _insert_users(self):
        users = [
            {'user_id': 1, 'first_name': 'jon', 'last_name': 'doe', 'email': 'jon.doe@gmail.com'},
            {'user_id': 2, 'first_name': 'anna', 'last_name': 'abc', 'email': 'anna.abc@gmail.com'},
            {'user_id': 3, 'first_name': 'anna', 'last_name': 'bcd', 'email': 'anna.bcd@gmail.com'}
        ]
        for user in users:
            self.fetch('/api/users', method='POST', body=json.dumps(user))
