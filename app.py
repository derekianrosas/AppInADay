from flask import Flask, render_template, request
from flask import Flask, request, jsonify, Request, flash, redirect, url_for, send_from_directory # Added flash, redirect, url_for and send_from_directory from flask documentation
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)
ma = Marshmallow(app)
heroku = Heroku(app)
CORS(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

    def __init__(self, name, data):
        self.name = name
        self.data = data

class FileSchema(ma.Schema):
    class Meta:
        fields = ["id", "name", "data"]

files_schema = FileSchema(many=True)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_addfile():
    if request.method == 'POST':
      f = request.files['file']
      
      newFile = File(name=f.filename, data=f.read())
      db.session.add(newFile)
      db.session.commit()

      return 'file uploaded successfully'

@app.route('/files/get', methods=['GET'])
def get_all_files():
    all_files = db.session.query(File.id, File.name, File.data).all()
    return jsonify(all_files)

    # return jsonify(files_schema.dump(all_files))

		
if __name__ == '__main__':
   app.run(debug = True)