import os
from flask import Flask
from flask_restx import Api
from mongoengine import connect
from config import Development as config
from v1.resources.routes import initialize_routes
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0, '/code')

app = Flask(__name__)
connect('app', host=config.MONGODB_URL)
api = Api(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
