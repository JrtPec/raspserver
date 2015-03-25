from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired as Required
from models import User

class LoginForm(Form):
	username = TextField('username', validators = [Required()])
	password = PasswordField('password', validators = [Required()])

	def validate(self):
		if not Form.validate(self):
			return False

		#fetch user
		user = User.query.filter_by(username=self.username.data).first()
		#check if user exists
		if user is None:
			self.username.errors.append('Username not found')
			return False
		#check if password is wrong
		elif not user.check_password(self.password.data):
			self.password.errors.append('Wrong password')
			return False
		#if all checks pass => validation True
		else:
			return True

class RegisterForm(Form):
	username = TextField('username', validators = [Required()])
	password = PasswordField('password', validators = [Required()])
	password2 = PasswordField('password2', validators = [Required()])

	def validate(self):
		if not Form.validate(self):
			return False

		#check if repeated password matches password
		if self.password.data != self.password2.data:
			self.password2.errors.append('Passwords do not match')
			return False

		#fetch user
		user = User.query.filter_by(username=self.username.data).first()
		
		#Check if username already exists
		if user is not None:
			self.username.errors.append('Username already exists')
			return False
		#if Username is unique => validation True
		else:
			return True

class EmptyForm(Form):
	pass

class DateTimeForm(Form):
	date = DateField('date', format='%Y-%m-%d')

class TrainForm(Form):
	date = DateField('date')
	origin = TextField('origin')
	destination = TextField('destination')
	delay = IntegerField('delay',)