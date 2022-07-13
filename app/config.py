from flask_sqlalchemy import SQLAlchemy
from os import environ

class Configuration:
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL") or \
        "postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    