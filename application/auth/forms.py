from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
  
class LoginForm(FlaskForm):

    username = StringField("Käyttäjätunnus", [validators.Length(min=1)])
    password = PasswordField("Salasana", [validators.Length(min=1)])
    
    class Meta:
        csrf = False

class UserForm(FlaskForm):
    firstname = StringField("Etunimi", [validators.Length(min=1)])
    surename = StringField("Sukunimi", [validators.Length(min=1)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=4)])
    password = PasswordField("Salasana", [validators.Length(min=10)])
    re_password = PasswordField("Salasana uudelleen", [validators.Length(min=10)])
    role = SelectField("Rooli", choices = [('basic', 'Peruskäyttäjä'), ('admin', 'Admin')])
    
    class Meta:
        csrf = False
  
class PasswordForm(FlaskForm):
    new_password = PasswordField("", [validators.Length(min=10)])
    new_password_again = PasswordField("",[validators.Length(min=10)])

    class Meta:
        csrf = False