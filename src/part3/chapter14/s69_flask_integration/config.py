import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'development key'
    ADMINS = frozenset(['jason@jasonmyers.com'])


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/dev.db'


class ProductionConfig(Config):
    SECRET_KEY = 'Prod key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/prod.db'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
