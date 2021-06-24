from sqlalchemy import Table, Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

from database.db import Base


class User(Base, SerializerMixin):

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    def __eq__(self, other):
        return type(self) == type(other) and \
                self.user_id == other.user_id and \
                self.first_name == other.first_name and \
                self.last_name == other.last_name and \
                self.email == other.email
