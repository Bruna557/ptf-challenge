from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import load_config


config = load_config()

engine = create_engine(config["database_url"])

Session = sessionmaker(bind=engine,expire_on_commit=False)
Base = declarative_base()

def clean_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
