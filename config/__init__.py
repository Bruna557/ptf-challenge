import os

from .dev import config as dev_config
from .prod import config as prod_config
from .test import config as test_config

def load_config():
    environment = os.environ.get("PYTHON_ENV") or "development"

    if environment == "development":
        return dev_config
    if environment == "production":
        return prod_config
    if environment == "test":
        return test_config