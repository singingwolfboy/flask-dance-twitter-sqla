import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersekrit'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWITTER_OAUTH_APP_KEY = os.environ.get('TWITTER_OAUTH_APP_KEY')
    TWITTER_OAUTH_APP_SECRET = os.environ.get('TWITTER_OAUTH_APP_SECRET')
