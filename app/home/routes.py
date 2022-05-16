from flask import request
from . import home

@home.route('/', methods=['GET'])
def index():
    return "Hello world, my friends"