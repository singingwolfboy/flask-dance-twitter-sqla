import os


class Config(object):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") or "supersekrit"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWITTER_OAUTH_CLIENT_KEY = os.environ.get("TWITTER_OAUTH_CLIENT_KEY")
    TWITTER_OAUTH_CLIENT_SECRET = os.environ.get("TWITTER_OAUTH_CLIENT_SECRET")
