# README
This project is a challenge from Power to Fly.

## Stack
- Python 3.8
- Flask
- SQLAlchemy
- PostgreSQL
- Redis
- Docker

## Running with Docker
Make sure you have Docker installed and running, than run:
```bash
$ docker compose up --build
```

## Running without Docker
After installing Python 3.8, install virtualenv:
```bash
$ pip install virtualenv
```

Create a virtual environment and activate it:
```bash
$ virtualenv venv
```
```bash
$ source venv/Scripts/activate
```

Next, install the requirements:
```bash
$ pip install -r requirements.txt
```

Run the application:
```bash
$ python server.py
```
