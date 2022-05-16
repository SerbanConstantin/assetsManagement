from flask import Flask

from .home import home as home_blueprint

from .config import Config

def createApp():
    app = Flask(__name__)
    app.secret_key = "okdjedeyfhb@124"
    app.config.from_object(Config)

    app.register_blueprint(home_blueprint)
    
    return app

app = createApp()
