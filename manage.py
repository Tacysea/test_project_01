from flask import Flask, session
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_session import Session
from flask_wtf import CSRFProtect

app = Flask(__name__)
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
app.config.from_object(config['development'])
CSRFProtect(app)
Session(app)


@app.route('/')
def index():
    session['name'] = 'python02'
    return 'hello world'

if __name__ == '__main__':
    print(app.url_map)
    manager.run()