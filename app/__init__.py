from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .home import home as home_blueprint
from .login import login as login_blueprint
from .register import register as register_blueprint

from .config import Config

#leg dintre manage si home, motorul app
#application configuration
def createApp():
    app = Flask(__name__)
    app.secret_key = "okdjedeyfhb@124"
    app.config.from_object(Config)
#db configuration
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

#db models
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64))
        email = db.Column(db.String(120))
        pass_hash = db.Column(db.String(128))

    class Asset(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        asset_name = db.Column(db.String(64))
        location = db.Column(db.String(128))
        updated = db.Column(db.String(128))
         

    app.register_blueprint(home_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(register_blueprint)
    return app

app = createApp()
