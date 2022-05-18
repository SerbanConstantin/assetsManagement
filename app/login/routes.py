from flask import redirect, request, render_template, redirect, session, url_for, session
from sqlalchemy import create_engine, text
from . import login
import hashlib
import os

@login.route('/login', methods=['GET'])
def login_index():
    if "error" in request.args:
        return render_template('login/loginForm.html', error=request.args["error"])
    else:
        return render_template('login/loginForm.html')

@login.route('/validate_login', methods=['POST'])
def validate_login():
    
    if not request.form['inputEmail']:
        return redirect(url_for('login.login_index', error="No email or password was provided"))

    if not request.form['inputPassword']:
        return redirect(url_for('login.login_index', error="No email or password was provided"))

    email = request.form["inputEmail"]
    password = hashlib.md5(request.form["inputPassword"].encode()).hexdigest()

    engine = create_engine(os.environ.get('DATABASE_URL'))
    sql = text("SELECT COUNT(*) FROM user WHERE email='"+ email +"' AND pass_hash='" + password + "'")

    result = engine.execute(sql).fetchall()
    
    for record in result:
        if record[0]>0:
            session['email'] = email
            return redirect(url_for('home.index'))
        else:
            error = "No user found"
            return redirect(url_for('login.login_index', error=error))

    return redirect(url_for('login.login_index', error="habar nu am!"))
