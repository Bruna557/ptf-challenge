from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

Base = declarative_base()

def get_session(connection_string):
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine,expire_on_commit=False)
    return Session(), engine

def create_db(engine):
    Base.metadata.create_all(engine)
