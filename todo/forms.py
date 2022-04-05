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