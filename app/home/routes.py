from flask import request, render_template
from . import home

@home.route('/', methods=['GET'])
def index():
    return render_template('/home/index.html')

