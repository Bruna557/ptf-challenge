import os

DEVELOPMENT = {
    'db_connection_string': 'postgresql://Bruna557:123456@postgresql:5432/ptw-challenge',
    'cache_host': 'redis',
    'cache_port': 6379,
    'cache_pwd': 'psw231377',
    'cache_expiration': 300
}

PRODUCTION = {
    'db_connection_string': 'postgresql://gzvotpmtidzuzw:fe9576c3424c1af6a57872f1fff35f726442cfed86ca4bbd8c73f4211a840433@ec2-3-213-85-90.compute-1.amazonaws.com:5432/dfdh2jgo9ajup6',
    'cache_host': 'ec2-3-215-18-238.compute-1.amazonaws.com',
    'cache_port': 15480,
    'cache_pwd': 'p64ed55c880ee88c02ff15f72903ef122ce4abccbea36708fea2b5c5bfe47efe9',
    'cache_expiration': 300
}

TEST = {
    'db_connection_string': 'sqlite:///:memory:?cache=shared',
    'cache_host': 'redis',
    'cache_port': 6379,
    'cache_pwd': 'psw231377',
    'cache_expiration': 300
}

ENVIRONMENT = os.environ.get('PYTHON_ENV')
APP_SETTINGS =  DEVELOPMENT if ENVIRONMENT == 'dev' else TEST if ENVIRONMENT == 'test' else PRODUCTION
