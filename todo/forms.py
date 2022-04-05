from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    description = StringField('description', [validators.Length(min=4, max=100), DataRequired()])
    submit = SubmitField(label='Submit')

class EditTaskForm(FlaskForm):
    task_id = IntegerField()
    description = StringField('description', [validators.Length(min=4, max=100), DataRequired()])
    submit = SubmitField(label='Submit')

class CompleteTaskForm(FlaskForm):
    task_id = IntegerField()
    submit = SubmitField(label='Submit')

class DeleteTaskForm(FlaskForm):
    task_id = IntegerField()
    submit = SubmitField(label='Delete')