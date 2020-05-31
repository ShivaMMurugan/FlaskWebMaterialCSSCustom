import os

from main_app import app
from main_app import render_template
from main_app import UserLoginForm
from main_app import request
from main_app import redirect
from main_app import url_for
from flask_pymongo import PyMongo

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mywebsite'
mongo_database = PyMongo(app)

@app.route('/home_page')
def home_page():

	form = UserLoginForm()

	return render_template('home_page.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():

	form = UserLoginForm()

	if request.method == 'POST':

		user_name = request.form.get('username')
		pwd = request.form.get('password')

		users = mongo_database.db.users.insert({'username': user_name,
			'password': pwd})

		if user_name and pwd:

			return redirect(url_for('login'))

	return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():

	form = UserLoginForm()

	if request.method == 'POST':

		existing_username = request.form.get('username')
		existing_userpassword = request.form.get('password')

		db_users = mongo_database.db.users.find()

		for data in db_users:

			if existing_username == data['username'] and existing_userpassword == data['password']:

				return redirect(url_for('home_page'))

		return redirect(url_for('register'))


	return render_template('login.html', form=form)


@app.route('/about')
def about():
	form = UserLoginForm()
	return render_template('about.html', form=form)