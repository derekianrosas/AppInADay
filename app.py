from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ""

db = SQLAlchemy(app)
ma = Marshmallow(app)
heroku = Heroku(app)
CORS(app)


#code goes here



#server running
if __name__ == "__main__":
    app.debug = True
    app.run()
