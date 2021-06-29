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
    'db_connection_string': 'postgres://qdccvmmrsbvbkf:22718362e21e56164c25abda03ea289a30559f23e6468a92909793a6f5e1a399@ec2-35-174-35-242.compute-1.amazonaws.com:5432/df9ai60u3rh6f2',
    'cache_host': 'ec2-3-215-18-238.compute-1.amazonaws.com',
    'cache_port': 15480,
    'cache_pwd': 'p64ed55c880ee88c02ff15f72903ef122ce4abccbea36708fea2b5c5bfe47efe9',
    'cache_expiration': 300
}

TEST = {
    'app_port': 8080,
    'db_connection_string': 'sqlite:///:memory:?cache=shared',
    'cache_host': 'redis',
    'cache_port': 6379,
    'cache_pwd': 'psw231377',
    'cache_expiration': 300
}

ENVIRONMENT = os.environ.get('PYTHON_ENV')
APP_SETTINGS =  DEVELOPMENT if ENVIRONMENT == 'dev' else TEST if ENVIRONMENT == 'test' else PRODUCTION
