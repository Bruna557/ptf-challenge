from os.path import dirname, join

config = {
    "port": 8080,
    "database_url": "sqlite:///" + join(dirname(dirname(__file__)), "database.sqlite")
}
