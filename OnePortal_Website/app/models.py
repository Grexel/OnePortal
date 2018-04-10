from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

#User Types
TYPE_ADMIN = 1
TYPE_TEACHER = 2
TYPE_PARENT = 3
TYPE_STUDENT = 4

#Models Classes
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_type = db.Column(db.Integer)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	email = db.Column(db.String(120), index=True, unique=True)
	firstname = db.Column(db.String(30))
	lastname = db.Column(db.String(30))
	street = db.Column(db.String(50))
	city = db.Column(db.String(30))
	state = db.Column(db.String(2))
	zip = db.Column(db.String(5))
	phone = db.Column(db.String(10))
	
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)

	posts = db.relationship('Post', backref='author', lazy='dynamic')
		
	def avatar(self, size):
		digest = md5(self.email.lower().encode('utf-8')).hexdigest()
		return 'https://www.gravatar.com/avatar/{}?d=retro&s={}'.format(digest,size)
	
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	
	def is_admin(self):
		return self.user_type == TYPE_ADMIN
	def is_teacher(self):
		return self.user_type == TYPE_TEACHER
	def is_parent(self):
		return self.user_type == TYPE_PARENT
	def is_student(self):
		return self.user_type == TYPE_STUDENT
		
	def __repr__(self):
		return '<User {}>'.format(self.username)
	
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Post {}>'.format(self.body)
		
#Models Functions
@login.user_loader
def load_user(id):
	return User.query.get(int(id))