from flask import render_template, flash, redirect, url_for
from app import mainApp
from app.forms import LoginForm

user = {'username' : '', 'password' : ''}
upcoming = [
			{'date' : '3/1/2018', 'title' : 'Project 2'},
			{'date' : '3/2/2018', 'title' : 'TGIF'},
			{'date' : '3/12/2018', 'title' : 'Spring Break'},
			{'date' : '1/19/2038', 'title' : 'End of Time'}
		]

@mainApp.route('/')
@mainApp.route('/index.htm')
def index():
	if user['username'] == "":
		return render_template('index.html',title="Home", upcoming = upcoming)
	else:
		return render_template('index.html',title="Home", user=user, upcoming = upcoming)

@mainApp.route('/logout', methods=['GET','POST'])
def logout():
	user['username'] = ""
	user['password'] = ""
	return redirect(url_for('index'))
	
@mainApp.route('/login.htm', methods=['GET','POST'])
def login():
	global user
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		user['username'] = form.username.data
		user['password'] = form.password.data
		if user['password'] == "admin":
			return redirect(url_for('admin'))
		elif user['password'] == "teacher":
			return redirect(url_for('teacher'))
		elif user['password'] == "student":
			return redirect(url_for('student'))
		elif user['password'] == "parent":
			return redirect(url_for('parent'))
		else:
			return redirect(url_for('index'))
	return render_template('login.html', title='Sign in',user = user, form=form, upcoming = upcoming)
	
@mainApp.route('/profile.htm')
@mainApp.route('/profile/<string:username>.htm')
def profile(username):
	return render_template('profile.html', title='Profile', user=user, upcoming = upcoming)

@mainApp.route('/admin.htm')
def admin():
	return render_template('admin.html', title="Admin", user=user, upcoming = upcoming)
	
@mainApp.route('/teacher.htm')
def teacher():
	return render_template('index.html', title="teacher", user=user, upcoming = upcoming)
	
@mainApp.route('/parent.htm')
def parent():
	return render_template('index.html', title="Parent", user=user, upcoming = upcoming)
	
@mainApp.route('/student.htm')
def student():
	return render_template('index.html', title="student", user=user, upcoming = upcoming)
	
@mainApp.route('/calendar.htm')
def adminCalendar():
	return render_template('adminCalendar.html', title="Admin - Calendar", user=user, upcoming = upcoming)
	
@mainApp.route('/upcomingDates.htm')
def adminUpcoming():
	return render_template('adminUpcoming.html', title="Admin - Upcoming Dates", user=user, upcoming = upcoming)
	
	
#ALL OF THE ADMIN PAGES
@mainApp.route('/adminParents.htm')
def adminParents():
	return render_template('adminParents.html', title="Admin - Parent Menu", user=user, upcoming = upcoming)
	
@mainApp.route('/adminParentsNew.htm')
def adminParentsNew():
	return render_template('adminParentsNew.html', title="Admin - New Parent", user=user, upcoming = upcoming)
	
@mainApp.route('/adminParentsSearch.htm')
def adminParentsSearch():
	return render_template('adminParentsSearch.html', title="Admin - Search Parents", user=user, upcoming = upcoming)
	
	
@mainApp.route('/adminStudents.htm')
def adminStudents():
	return render_template('adminStudents.html', title="Admin - Student Menu", user=user, upcoming = upcoming)
@mainApp.route('/adminStudentsNew.htm')
def adminStudentsNew():
	return render_template('adminStudentsNew.html', title="Admin - New Student", user=user, upcoming = upcoming)
	
@mainApp.route('/adminStudentsSearch.htm')
def adminStudentsSearch():
	return render_template('adminStudentsSearch.html', title="Admin - Search Students", user=user, upcoming = upcoming)
	
	
@mainApp.route('/adminCourses.htm')
def adminCourses():
	return render_template('adminCourses.html', title="Admin - Course Changes", user=user, upcoming = upcoming)
	
@mainApp.route('/adminClasses.htm')
def adminClasses():
	return render_template('adminClasses.html', title="Admin - Classes Menu", user=user, upcoming = upcoming)
	
@mainApp.route('/adminClassesView.htm')
def adminClassesView():
	return render_template('adminClassesView.html', title="Admin - View Classes", user=user, upcoming = upcoming)
	
@mainApp.route('/adminClassesGenerate.htm')
def adminClassesGenerate():
	return render_template('adminClassesGenerate.html', title="Admin - Generate Classes", user=user, upcoming = upcoming)
	
@mainApp.route('/adminForms.htm')
def adminForms():
	return render_template('adminForms.html', title="Admin - Forms", user=user, upcoming = upcoming)
@mainApp.route('/adminFormsNew.htm')
def adminFormsNew():
	return render_template('adminFormsNew.html', title="Admin - New Form", user=user, upcoming = upcoming)
@mainApp.route('/adminFormsSearch.htm')
def adminFormsView():
	return render_template('adminFormsView.html', title="Admin - View Forms", user=user, upcoming = upcoming)
	
@mainApp.route('/adminReports.htm')
def adminReports():
	return render_template('adminReports.html', title="Admin - Reports", user=user, upcoming = upcoming)
@mainApp.route('/adminReportsAccounts.htm')
def adminReportsAccounts():
	return render_template('adminReportsAccounts.html', title="Admin - Report Accounts", user=user, upcoming = upcoming)
@mainApp.route('/adminReportsFailing.htm')
def adminReportsFailing():
	return render_template('adminReportsFailing.html', title="Admin - Report Failing", user=user, upcoming = upcoming)
@mainApp.route('/adminReportsTardy.htm')
def adminReportsTardy():
	return render_template('adminReportsTardy.html', title="Admin - Report Tardy", user=user, upcoming = upcoming)
@mainApp.route('/adminReportsEnrollment.htm')
def adminReportsEnrollment():
	return render_template('adminReportsEnrollment.html', title="Admin - Report Enrollment", user=user, upcoming = upcoming)