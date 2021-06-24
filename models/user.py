from sqlalchemy import Table, Column, Integer, String

from database.db import Base


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    birthday = Column(String)

    def __eq__(self, other):
        return type(self) == type(other) and \
                self.user_id == other.user_id and \
                self.first_name == other.first_name and \
                self.last_name == other.last_name and \
                self.email == other.email and \
                self.birthday == other. birthday

    def to_dict(self):
       return {c.name: unicode(getattr(self, c.name)) for c in self.__table__.columns}
