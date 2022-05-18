from flask import redirect, request, render_template, session, url_for
from sqlalchemy import create_engine, text
from . import home
import os

@home.route('/', methods=['GET'])
def index():
    if 'email' in session:
        email = session['email']
    else:
        email = None
    if email is None:
        return redirect(url_for('login.login_index'))
    else:
        engine = create_engine(os.environ.get('DATABASE_URL'))
        sql = text("SELECT * FROM asset") 
        result = engine.execute(sql).fetchall()

        return render_template('home/index.html', assets=result, email=email)

@home.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('login.login_index'))

@home.route('/create', methods=['GET','POST'])
def insert():
    if "nameInput" in request.form:
        name = request.form['nameInput']
        location = request.form['locationInput']

        if "updatedInput" in request.form:
            updated = True
        else:
            updated = False

        engine = create_engine(os.environ.get('DATABASE_URL'))
        sql = text("INSERT INTO asset (asset_name, location, updated) VALUES (:a, :l, :u)")
        try:
            engine.execute(sql, a=name, l=location, u=updated)
        except ValueError:
            return ValueError

        return redirect(url_for('home.index'))
    else:
        return render_template('home/insert.html')

@home.route('/delete', methods=['GET','POST'])
def delete():
    engine = create_engine(os.environ.get('DATABASE_URL'))
    if "nameInput" in request.form:
        name = request.form["nameInput"]

        sql = text("DELETE FROM asset WHERE asset_name='"+ name + "'")
        try:
            engine.execute(sql)
        except ValueError:
            return ValueError
        return redirect(url_for('home.index'))
    else:
        sql = text("SELECT asset_name from asset")
        result = engine.execute(sql).fetchall()
        return render_template('home/delete.html', assets=result)

