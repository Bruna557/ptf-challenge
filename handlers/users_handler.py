from .crud_handler import CrudHandler


class UsersHandler(CrudHandler):

    def initialize(self, repository):
        self.repository = repository
