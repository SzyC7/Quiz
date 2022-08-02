import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or ("sqlite:///data.db")
    DEBUG = os.environ.get("BUG_SET")
    DEVELOPMENT = os.environ.get("DEV_SET")
    FLASK_HTPASSWD_PATH = "/secret/.htpasswd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "do-i-really-need-this"