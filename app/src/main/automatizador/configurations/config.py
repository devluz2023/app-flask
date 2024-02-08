import os
import random, string


class Config(object):
    CSRF_ENABLED = True,
    CORS_ENABLED = False
    SQLALCHEMY_DATABASE_URI_DOCKER = \
        '{SGBD}://{usuario}:{senha}@{servidor}/{database}?DRIVER={driver}'.format(
            driver='FreeTDS',
            SGBD='mssql+pyodbc',
            usuario='sa',
            senha='Your_Password_123',
            servidor='db, 1433',
            database='valeEY'

        )

    SQLALCHEMY_DATABASE_URI_LOCAL = \
        '{SGBD}://{usuario}:{senha}@{servidor}/{database}?DRIVER={driver}'.format(
            driver='SQL+Server+Native+Client+11.0',
            SGBD='mssql+pyodbc',
            usuario='sa',
            senha='Your_Password_123',
            servidor='127.0.0.1, 1433',
            database='valeEY'

        )
    ROOT_DIR = os.path.dirname("C:\\automatizador\\app2")
    APP = None


class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True
    IP_HOST = '0.0.0.0'
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = '0.0.0.0'  # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = '0.0.0.0'  # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')

