from mock import MagicMock
from random import randint
from unittest import TestCase

from persistence import repository
from models.user import User


class TestRepository(TestCase):
    def test_get_all(self):
        offset = randint(1, 10)
        limit = randint(1,10)

        session_mock = MagicMock()
        session_mock.query\
            .return_value.filter_by\
            .return_value.offset\
            .return_value.limit\
            .return_value.all\
            .return_value = [User()]*(limit+1)

        repo = repository.Repository(entity=User, session=session_mock)

        result = repo.get_all(offset, limit)

        self.assertEqual(limit, len(result['data']))
        self.assertTrue(result['next_page'])

    def test_get_all_should_return_next_page_false(self):
        offset = randint(1, 10)
        limit = randint(1,10)

        session_mock = MagicMock()
        session_mock.query\
            .return_value.filter_by\
            .return_value.offset\
            .return_value.limit\
            .return_value.all\
            .return_value = [User()]*limit

        repo = repository.Repository(entity = User, session = session_mock)

        result = repo.get_all(offset, limit)

        self.assertEqual(limit, len(result['data']))
        self.assertFalse(result['next_page'])
