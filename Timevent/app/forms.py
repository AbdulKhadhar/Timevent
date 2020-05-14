from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired()])
	password=PasswordField('Password', validators=[DataRequired()])
	remember_me=BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class InputEvent(FlaskForm):
	TitleOfEvent = StringField(label='Title of Event',validators=[DataRequired()])
	Discription = StringField(label='Disription of Event',validators=[DataRequired()])
	DateOfEvent = DateField(label='Date of Event',validators=[DataRequired()])
