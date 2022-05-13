import re
from flask import Flask

from .config import Config

app = Flask(__name__)
app.secret_key = "okdjedeyfhb@124"
app.config.from_object(Config)

def createApp():
    return app
