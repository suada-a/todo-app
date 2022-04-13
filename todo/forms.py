from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired, EqualTo, Email, ValidationError
from todo.models import User

class AddTaskForm(FlaskForm):
    user_id = IntegerField()
    description = StringField('description', validators=[Length(min=4, max=100), DataRequired()])
    submit = SubmitField(label='Submit')

class EditTaskForm(FlaskForm):
    task_id = IntegerField()
    description = StringField('description', validators=[Length(min=4, max=100), DataRequired()])
    submit = SubmitField(label='Submit')

class CompleteTaskForm(FlaskForm):
    task_id = IntegerField()
    submit = SubmitField(label='Submit')

class DeleteTaskForm(FlaskForm):
    task_id = IntegerField()
    submit = SubmitField(label='Delete')

class RegisterForm(FlaskForm):
    def validate_username(self, unchecked_username):
        user = User.query.filter_by(username=unchecked_username.data).first()

        if user:
            raise ValidationError('Username already exists. Please try a different username')

    def validate_email_address(self, unchecked_email_address):
        email_address = User.query.filter_by(email_address=unchecked_email_address.data).first()

        if email_address:
            raise ValidationError('Email address already exists. Please try a different email address')

    username = StringField('Username', validators=[Length(min=4, max=100), DataRequired()])
    email_address = StringField('Email Address', validators=[Email()])
    password = PasswordField('Password', validators=[Length(min=6, max=100), DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')