from sre_constants import SUCCESS
from flask import redirect, request, render_template, redirect, url_for
import hashlib
import os
from sqlalchemy import create_engine, text

from . import register

@register.route('/register', methods=['GET'])
def register_index():
    return render_template('register/registerform.html')

@register.route('/handle_register', methods=['POST'])
def handle_register():
    if not request.form['inputEmail']:
        return redirect(url_for('login.login_index', error="No email, name or password was provided"))
    if not request.form['inputName']:
        return redirect(url_for('login.login_index', error="No email, name or password was provided"))
    if not request.form['inputPassword']:
        return redirect(url_for('login.login_index', error="No email, name or password was provided"))

    email = request.form["inputEmail"]
    name = request.form['inputName']
    password = hashlib.md5(request.form["inputPassword"].encode()).hexdigest()

    engine = create_engine(os.environ.get('DATABASE_URL'))
    sql = text("INSERT INTO user (username, email, pass_hash) VALUES (:u, :e, :p)")

    try:
        engine.execute(sql, u=name, e=email, p=password)
    except ValueError:
        return ValueError

    return redirect(url_for('login.login_index', error=SUCCESS))
