from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class CommentForm(FlaskForm):

    text = TextAreaField(id = 'text')
    
    class Meta:
        csrf = False
    
