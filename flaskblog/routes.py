from flask import render_template, jsonify, request, flash, redirect, url_for
from flaskblog import app, api
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.database import posts
from flaskblog.resources.post import PostSimple
import json


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def registration():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == "password":
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Invaid email or password', 'danger')
	return render_template('login.html', title='Login', form=form)


api.add_resource(PostSimple, '/api/v1/posts')