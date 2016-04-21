from uuid import uuid4
import os

basedir = os.path.abspath(os.path.dirname(__file__))
secret_key = str(uuid4())


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secret_key
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'sqlite:///../data-dev.db')
    MAX_BOARD_SIZE = 10
    MAX_DB_STRING_SIZE = MAX_BOARD_SIZE ** 2 * 4


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'sqlite:///../data-test.db')
    MAX_BOARD_SIZE = 10
    MAX_DB_STRING_SIZE = MAX_BOARD_SIZE ** 2 * 4

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
