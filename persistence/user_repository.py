from .repository import Repository
from models.user import User

class UserRepository(Repository):
    entity = User
