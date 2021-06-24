from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_name = 'ptw-challenge'
db_user = 'Bruna557'
db_pass = '123456'
db_host = 'postgresql'
db_port = '5432'
db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

engine = create_engine(db_string)

Session = sessionmaker(bind=engine,expire_on_commit=False)
Base = declarative_base()
