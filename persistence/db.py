from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings


db_string = f'postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PWD}' \
            f'@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_NAME}'

engine = create_engine(db_string)

Session = sessionmaker(bind=engine,expire_on_commit=False)
Base = declarative_base()
