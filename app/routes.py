from flask import Flask, render_template, request, redirect, flash , url_for
from app import app, forms, db
from app.forms import LoginForm, InputEvent, RegistrationForm
from flask_login import login_required,current_user, login_user, logout_user, login_manager
from werkzeug.urls import url_parse
from app.models import User, Post

#methods=['GET','POST']
@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
@login_required
def index():
	#if current_user.is_authenticated:
	form = InputEvent()
	if form.validate_on_submit():
		posts = Post(body=form.TitleOfEvent.data, discription=form.Discription.data, author=user)
#,timestamp=form.DateOfEvent.data
		db.session.add(posts)
        	db.session.commit()
		flash('Added a new Event')
        	return redirect(url_for('display'))
#,body=body,discription=discription, timestamp=timestamp,user=user,posts=posts
		#return render_template('display.html',body=body,discription=discription, user=user)
	return render_template('index.htm',form=form)

	#form = InputEvent()
	#if form.validate_on_submit():
		#flash('Event with title TitleOfEvent {}, TitleOfEvent={}'.format(
		#form.TitleOfEvent.data, form.TitleOfEvent.data))
		#print("Form correct")
		#title = request.form['TitleOfEvent']
		#discription = request.form['Discription']
		#date = request.form['DateOfEvent']
		#return redirect('/display')
		#return render_template('display.html',title=title,discription=discription, date=date)
	#return render_template('index.htm',form=form)
	#return render_template('index.htm', title='Add Event', form=form)
	#user ={'username':'Abdu'}
	#if request.method == 'POST' and form.validate():
		#posts=addevent([{'author': {'username':form.T.data}, 'body':form.D.data,'date':form.DD.data}])
		#TitleOfEvent = form.TitleOfEvent.data
		#Discription = form.Discription.data
		#DateOfEvent = form.DateOfEvent.data
		#posts= InputEvent(	TitleOfEvent = TitleOfEvent,
			 		#Discription = Discription,
			 		#DateOfEvent = DateOfEvent	)

	#else:
		#posts= []
	#posts=[{'author': {'username':'Enfa'}, 'body':'Hola'},{'author': {'username':'Ann'}, 'body':'Myavo'}]
		#return render_template('index.htm',title='Home',user=user, posts=posts, form=form)
		#return render_template('display.htm',user=user, posts=posts)
	#return render_template('index.htm', form=form)

@app.route('/display', methods=['GET','POST'])
def display():
    user = User.query.filter_by(current_user).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('display.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
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
    return render_template('login.htm', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/about')
def about():
	return render_template('about.htm', title='About - Timevent')


