from flask import Flask, render_template, request, redirect
from app import app, forms
from app.forms import LoginForm, InputEvent

@app.route('/', methods=['GET','POST'])
#@app.route('/index')
def index():
	form = InputEvent()
	if form.validate_on_submit():
		#flash('Event with title TitleOfEvent {}, TitleOfEvent={}'.format(
		#form.TitleOfEvent.data, form.TitleOfEvent.data))
		print("Form correct")
		title=request.form['TitleOfEvent']
		discription = request.form['Discription']
		date = request.form['DateOfEvent']
		#return redirect('/display')
		return render_template('display.html',title=title,discription=discription, date=date)
	return render_template('index.htm', form=form)
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
	display = InputEvent()
	return render_template('display.html', display=display)

@app.route('/login')
def login():
	form=LoginForm()
	return render_template('login.htm', title='Sign In', form=form)

@app.route('/about')
def about():
	return render_template('about.htm', title='About - Timevent')


