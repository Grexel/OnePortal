from app import mainApp, db
from app.models import User, Post

@mainApp.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post':Post}