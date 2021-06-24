from logzero import logger
from sqlalchemy.orm.exc import NoResultFound
from contextlib import contextmanager

from exception.enitity_not_found import EntityNotFound
from database.db import Session

class BaseRepository():

    entity = NotImplementedError

    @contextmanager
    def command_session_scope(self):
        '''Provide a transactional scope around a series of operations.'''
        session = Session()
        try:
            yield session
            session.commit()
        except Exception as err:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def query_session_scope(self):
        '''Provide a transactional scope around a series of operations.'''
        session = Session()
        session.expire_on_commit = False
        try:
            yield session
        except Exception as err:
            raise
        finally:
            session.close()

    def get_all(self):
        with self.query_session_scope() as session:
            return session.query(self.entity).all()

    def get_by_id(self, entity_id):
        with self.query_session_scope() as session:
            result = session.query(self.entity).get(entity_id)
            if not result:
                raise EntityNotFound
            return result

    def save(self, entity):
        with self.command_session_scope() as session:
            return session.add(self.entity(**entity))
