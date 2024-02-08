import os

from flask import Flask
from importlib import reload
import sys
from src.main.automatizador.controllers.base.FaseController import faseapp
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from src.main.automatizador.configurations.config import app_config, app_active


config = app_config[app_active]

app = Flask(__name__)

app.config.from_object(app_config[app_active])
app.register_blueprint(faseapp, url_prefix='/fase')
app.config.from_pyfile('src\\main\\automatizador\\configurations\\config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI_LOCAL
if os.getenv('PLATFORM') == 'DOCKER':
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI_DOCKER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(config.APP)
# migrate = Migrate(app, db)
CORS(app)
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! '
@app.route('/teste')
def teste():  # put application's code here
    return 'teste! '

if __name__ == '__main__':
    app.run(host=config.IP_HOST, port=config.PORT_HOST)
    reload(sys)