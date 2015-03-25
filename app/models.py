from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True, nullable=False)
	pw_hash = db.Column(db.String(160), nullable=False)
	role = db.Column(db.Integer, default=ROLE_USER)
	created = db.Column(db.DateTime)
	trains = db.relationship('Train', backref='user', lazy='dynamic', cascade="all,delete,delete-orphan")

	@staticmethod
	def get_pw_hash(password):
		return generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pw_hash, password)

	def is_admin(self):
		if self.role == ROLE_ADMIN:
			return True
		else:
			return False

	def make_admin(self):
		self.role = ROLE_ADMIN

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def get_id(self):
		return unicode(self.id)

	def is_anonymous(self):
		return False

class Train(db.Model):
	__tablename__ = 'train'
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	created = db.Column(db.DateTime)
	date = db.Column(db.Date)
	origin = db.Column(db.String(64))
	destination = db.Column(db.String(64))
	delay = db.Column(db.Integer, default=0)