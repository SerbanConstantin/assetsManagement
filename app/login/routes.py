from flask import request, render_template
from . import login

@login.route('/login', methods=['GET'])
def login():
    return render_template('/login/loginform.html')