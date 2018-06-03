from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(config[config_name])
    CSRFProtect(app)
    Session(app)

    return app