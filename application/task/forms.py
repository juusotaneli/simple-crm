from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    date = DateField('DatePicker', format='%Y-%m-%d', validators = [DataRequired(), validators.length(min=1)])
    task_comment = TextAreaField(id='task_comment', validators = [DataRequired(), validators.length(min=1)])
    

    class Meta:
        csrf = False