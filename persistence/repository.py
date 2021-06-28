from exception.enitity_not_found import EntityNotFound


class Repository():
    entity = None
    session = None

    def __init__(self, entity, session):
        self.entity = entity
        self.session = session

    def get_all(self, offset, limit, **kwargs):
        result = self.session.query(self.entity).filter_by(**kwargs).offset(offset).limit(limit+1).all()
        if next_page := len(result) > limit:
            result = result[:-1]
        return {'data': [row.to_dict() for row in result], 'next_page': next_page}

    def get_by_id(self, entity_id):
        result = self.session.query(self.entity).get(entity_id)
        if not result:
            raise EntityNotFound
        return result.to_dict()

    def save(self, entity):
        try:
            self.session.add(self.entity(**entity))
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise
