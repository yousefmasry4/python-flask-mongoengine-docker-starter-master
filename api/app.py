import os
from flask import Flask
from flask_restx import Api
from mongoengine import connect
from config import BaseConfig, Development as config
from v1.resources.routes import initialize_routes
# some_file.py
import sys


app = Flask(__name__,static_url_path='',static_folder='../uploads/',)
print(app.static_folder)
connect(host=config.MONGODB_URL)
# Create directory
dirName = '../uploads'
try:
    # Create target Directory
    os.mkdir(os.getcwd()+'/'+dirName)
except FileExistsError:
    print("Directory " , dirName ,  " already exists")
api = Api(app)

initialize_routes(api)


if __name__ == "__main__":
    app.run(BaseConfig.HOST,port=BaseConfig.PORT, debug=True)
