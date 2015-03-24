from app import app, lm, db
from flask import render_template, flash, redirect, url_for, g, request
from models import User
from flask.ext.login import current_user, login_required, login_user, logout_user
from forms import LoginForm, RegisterForm

@app.before_request
def before_request():
	g.user = current_user

@lm.user_loader
def load_user(id):
	return User.query.get(id)

#HTTP ERRORS
@app.errorhandler(404)
def internal_error(error):
	flash('404 - Page not found')
	return redirect(url_for('index'))
@app.errorhandler(500)
def internal_error(error):
	#db.session.rollback()
	flash('500 - Server error')
	return redirect(url_for('index'))

@app.route('/login', methods = ['GET','POST'])
def login():
	'''
		Creates LogIn page + processes LogIn form
	'''

	#redirect if user is already logged in
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))

	#init form
	form = LoginForm()		

	#find user, log him in and redirect to next page or index
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		login_user(user)
		return redirect(request.args.get('next') or url_for('index'))

	#if there is no post, generate log in page
	return render_template(
			'login.html',
			title = 'Log In',
			form=form)

@app.route('/logout')
@login_required
def logout():
	"""
		Log Out user
	"""
	logout_user()
	flash('Logout successful')
	return redirect(url_for('login'))

@app.route('/register', methods = ['GET','POST'])
def register():
	"""
		Make register form and create new user
	"""
	#redirect if user is already logged in
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))

	#init form
	form = RegisterForm()

	#process posted form, create new user, add to db, and log him in
	if form.validate_on_submit():
		#generate hash for password
		pw_hash = User.get_pw_hash(form.password.data)

		newuser = User(username=form.username.data,pw_hash=pw_hash)
		
		db.session.add(newuser)
		db.session.commit()

		login_user(newuser)

		return redirect(url_for('index'))

	#if there is no post, present register form
	return render_template(
		'register.html',
		title='Register',
		form = form)

@app.route('/')
@app.route('/index')
@login_required
def index():
	"""
		MAIN PAGE
	"""
	return render_template(
		'index.html')

@app.route('/serverlogs')
@login_required
def serverlogs():
	"""
		Download links for different log files
	"""
	return render_template(
		'serverlogs.html',
		title='Server Logs')