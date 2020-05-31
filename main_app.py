from models import UserLoginForm
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_material import Material

app = Flask(__name__)

material = Material(app)

app.config.from_pyfile('config.py')

''' Importing views below to avoid circular import error, 
	there is also a better way of doing this, but I don't 
    want to use package strucute etc..
'''
from views import *

if __name__ == '__main__':

	app.run(debug=True)