import glob
import importlib
import os
from flask import Flask, jsonify
from flask_cors import CORS
from src.database.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'secret'
CORS(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'}), 200

""" Automatically import controller files """
for controller_file in glob.glob(os.path.dirname(__file__) + "/**/*_controller.py", recursive=True):
    abs_module_location = importlib.util.spec_from_file_location(os.path.basename(controller_file)[:-3], controller_file)
    abs_module_location.loader.exec_module(importlib.util.module_from_spec(abs_module_location))