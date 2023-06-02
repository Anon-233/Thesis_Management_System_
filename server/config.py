import os

# JWT
JWT_SECRET_KEY = os.urandom(24)

# DataBase
def init(_config: str = './_config.init'):
    global username, password, ip_address, port, database
    info = open(_config, 'r')
    read = lambda: info.readline().strip('\n')
    username = read()
    password = read()
    ip_address = read()
    port = read()
    database = read()

init()
db_uri = f'postgresql://{username}:{password}@{ip_address}:{port}/{database}'

class Config:
    pass

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'production': ProductionConfig,
    'devlopment': DevelopmentConfig,
}