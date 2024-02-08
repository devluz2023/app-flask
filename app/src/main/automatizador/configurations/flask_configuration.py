# -*- coding: utf-8 -*-
# config import
import os
from flask import Flask
from flask_cors import CORS
from src.main.automatizador.configurations.config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

config = app_config[app_active]


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI_LOCAL
    if os.getenv('PLATFORM')=='DOCKER':
         app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI_DOCKER
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(config.APP)
    migrate = Migrate(app, db)
    CORS(app)

    db.init_app(app)

    @app.route("/")
    def index():
        return "Flask inside Docker!!"

    return app
