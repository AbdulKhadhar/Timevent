from flask import Flask, render_template, request, redirect
from app import app, forms
from app.forms import LoginForm, InputEvent

@app.route('/', methods=['GET','POST'])
def index():
	form = InputEvent()
	if form.validate_on_submit():
		print("Form correct")
		title=request.form['TitleOfEvent']
		discription = request.form['Discription']
		date = request.form['DateOfEvent']
		return render_template('display.html',title=title,discription=discription, date=date)
	return render_template('index.htm', form=form)

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


