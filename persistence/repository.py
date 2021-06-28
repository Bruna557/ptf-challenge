from contextlib import contextmanager

from exception.enitity_not_found import EntityNotFound
from persistence.db import Session


class Repository():
    entity = NotImplementedError

    @contextmanager
    def command_session_scope(self):
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
        session = Session()
        session.expire_on_commit = False # avaliar tirar
        try:
            yield session
        except Exception as err:
            raise
        finally:
            session.close()

    def get_all(self, offset, limit, **kwargs):
        with self.query_session_scope() as session:
            result = session.query(self.entity).filter_by(**kwargs).offset(offset).limit(limit+1).all()
            if next_page := len(result) > limit:
                result = result[:-1]
            return {'data': [row.to_dict() for row in result], 'next_page': next_page}

    def get_by_id(self, entity_id):
        with self.query_session_scope() as session:
            result = session.query(self.entity).get(entity_id)
            if not result:
                raise EntityNotFound
            return result.to_dict()

    def save(self, entity):
        with self.command_session_scope() as session:
            return session.add(self.entity(**entity))
