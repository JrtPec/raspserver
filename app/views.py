from app import app
from flask import render_template, flash, redirect, url_for

@app.errorhandler(404)
def internal_error(error):
	flash('404 - Page not found')
	return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
def index():
	return render_template(
		'index.html')