# README
This project is a challenge from Power to Fly.

## Stack
- Python 3.8
- Tornado
- SQLAlchemy
- PostgreSQL
- Redis
- Docker

## Running
Make sure you have Docker installed and running.
```bash
$ docker compose up --build
```

## Running tests
### Setup
Install Python 3.8 and virtualenv (`$ pip install virtualenv`).
Then, create a virtual environment and activate it (on Windows, use CMD to create the virtual environment):
```bash
$ virtualenv venv
$ source venv/Scripts/activate
```

Install requirements:
```bash
$ pip install -r requirements.txt
```

### Run
To run all tests, from `ptw-challenge` run:
```bash
$ python -m unittest
```

To run a single test:
```bash
$ python -m unittest test.file.Class.test
```

## Dev Notes
For Redis GUI access [Redsmin](https://app.redsmin.com/), create an account and create a connection of type 'Localhost Redis'. Copy the proxy connection key. Install the proxy and run:
```bash
$ npm install redsmin@latest -g
$ REDSMIN_KEY=<proxy_connection_key> REDIS_AUTH=<password> redsmin
```
