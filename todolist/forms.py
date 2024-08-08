from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Optional ,Length


class LoginForm(FlaskForm):
    nick_name = StringField('Nick name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    nick_name = StringField('Nick Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class TaskForm(FlaskForm):
    task = StringField('Task', validators=[Optional(), Length(min=5, max=100)])


class WeekForm(FlaskForm):
    monday = StringField('Monday')
    tuesday = StringField('Tuesday')
    wednesday = StringField('Wednesday')
    thursday = StringField('Thursday')
    friday = StringField('Friday')
    saturday = StringField('Saturday')
    sunday = StringField('Sunday')
