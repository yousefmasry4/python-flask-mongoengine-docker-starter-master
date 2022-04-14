import os
from flask import Flask
from flask_restx import Api
from mongoengine import connect
from config import Development as config
from v1.resources.routes import initialize_routes
# some_file.py
import sys

sys.path.insert(0, '/code')

app = Flask(__name__)
print(config.MONGODB_URL)
connect(host=config.MONGODB_URL)

api = Api(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run()
