from . import blu
from flask import session

@blu.route('/')
def index():
    session['name'] = 'python02'
    return 'hello world'