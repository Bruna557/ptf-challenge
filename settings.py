import os

DEVELOPMENT = {
    'app_port': 8080,
    'db_connection_string': 'postgresql://Bruna557:123456@postgresql:5432/ptw-challenge',
    'cache_host': 'redis',
    'cache_port': 6379,
    'cache_pwd': 'psw231377',
    'cache_expiration': 300
}

PRODUCTION = {
    'app_port': 8080,
    'db_connection_string': 'postgresql://Bruna557:123456@postgresql:5432/ptw-challenge',
    'cache_host': 'redis',
    'cache_port': 6379,
    'cache_pwd': 'psw231377',
    'cache_expiration': 300
}

TEST = {
    'app_port': 8080,
    'db_connection_string': 'sqlite:///:memory:?cache=shared',
    'cache_host': '',
    'cache_port': 6379,
    'cache_pwd': 'psw231377',
    'cache_expiration': 300
}

ENVIRONMENT = os.environ.get('PYTHON_ENV')
APP_SETTINGS =  PRODUCTION if ENVIRONMENT == 'production' else TEST if ENVIRONMENT == 'test' else DEVELOPMENT
