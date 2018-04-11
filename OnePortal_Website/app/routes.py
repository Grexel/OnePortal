from flask import render_template, flash, redirect, url_for
from app import mainApp, login, db
from app.forms import LoginForm

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, TYPE_ADMIN

from flask import request
from werkzeug.urls import url_parse

from datetime import datetime


upcoming = [
			{'date' : '3/1/2018', 'title' : 'Project 2'},
			{'date' : '3/2/2018', 'title' : 'TGIF'},
			{'date' : '3/12/2018', 'title' : 'Spring Break'},
			{'date' : '1/19/2038', 'title' : 'End of Time'}
		]

@mainApp.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()

@mainApp.route('/')
@mainApp.route('/index')
@login_required
def index():
	#render a different page based on each user_type
	if current_user.is_admin():
		return redirect(url_for('admin'))
	elif current_user.is_teacher():
		return redirect(url_for('teacher'))
	elif current_user.is_parent():
		return redirect(url_for('parent'))
	elif current_user.is_student():
		return redirect(url_for('student'))
	else: #This should only happen if the user_type isn't set properly
		return render_template('index.html',title="Home", user=current_user, upcoming = upcoming)

@mainApp.route('/logout', methods=['GET','POST'])
def logout():
	logout_user()
	return redirect(url_for('index'))
	
@mainApp.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign in', form=form)
	
@mainApp.route('/profile')
@mainApp.route('/profile/<string:username>')
def profile(username):
	user = User.query.filter_by(username=username).first_or_404()
	return render_template('profile.html', title='Profile', user=current_user, upcoming = upcoming)

@mainApp.route('/admin')
def admin():
	return render_template('admin.html', title="Administrator", user=current_user, upcoming = upcoming)
	
@mainApp.route('/teacher')
def teacher():
	return render_template('teacher.html', title="Teacher", user=current_user, upcoming = upcoming)
	
@mainApp.route('/parent')
def parent():
	return render_template('parent.html', title="Parent", user=current_user, upcoming = upcoming)
	
@mainApp.route('/student')
def student():
	return render_template('student.html', title="Student", user=current_user, upcoming = upcoming)
	
@mainApp.route('/calendar')
def adminCalendar():
	return render_template('adminCalendar.html', title="Admin - Calendar", user=current_user, upcoming = upcoming)
	
@mainApp.route('/upcomingDates')
def adminUpcoming():
	return render_template('adminUpcoming.html', title="Admin - Upcoming Dates", user=current_user, upcoming = upcoming)
	
	
#ALL OF THE ADMIN PAGES
@mainApp.route('/adminParents')
def adminParents():
	return render_template('adminParents.html', title="Admin - Parent Menu", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminParentsNew')
def adminParentsNew():
	return render_template('adminParentsNew.html', title="Admin - New Parent", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminParentsSearch')
def adminParentsSearch():
	return render_template('adminParentsSearch.html', title="Admin - Search Parents", user=current_user, upcoming = upcoming)
	
	
@mainApp.route('/adminStudents')
def adminStudents():
	return render_template('adminStudents.html', title="Admin - Student Menu", user=current_user, upcoming = upcoming)
@mainApp.route('/adminStudentsNew')
def adminStudentsNew():
	return render_template('adminStudentsNew.html', title="Admin - New Student", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminStudentsSearch')
def adminStudentsSearch():
	return render_template('adminStudentsSearch.html', title="Admin - Search Students", user=current_user, upcoming = upcoming)
	
	
@mainApp.route('/adminCourses')
def adminCourses():
	return render_template('adminCourses.html', title="Admin - Course Changes", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminClasses')
def adminClasses():
	return render_template('adminClasses.html', title="Admin - Classes Menu", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminClassesView')
def adminClassesView():
	return render_template('adminClassesView.html', title="Admin - View Classes", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminClassesGenerate')
def adminClassesGenerate():
	return render_template('adminClassesGenerate.html', title="Admin - Generate Classes", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminForms')
def adminForms():
	return render_template('adminForms.html', title="Admin - Forms", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminFormsNew')
def adminFormsNew():
	return render_template('adminFormsNew.html', title="Admin - New Form", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminFormsSearch')
def adminFormsView():
	return render_template('adminFormsView.html', title="Admin - View Forms", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminReports')
def adminReports():
	return render_template('adminReports.html', title="Admin - Reports", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminReportsAccounts')
def adminReportsAccounts():
	return render_template('adminReportsAccounts.html', title="Admin - Report Accounts", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminReportsFailing')
def adminReportsFailing():
	return render_template('adminReportsFailing.html', title="Admin - Report Failing", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminReportsTardy')
def adminReportsTardy():
	return render_template('adminReportsTardy.html', title="Admin - Report Tardy", user=current_user, upcoming = upcoming)
	
@mainApp.route('/adminReportsEnrollment')
def adminReportsEnrollment():
	return render_template('adminReportsEnrollment.html', title="Admin - Report Enrollment", user=current_user, upcoming = upcoming)
	