from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo,Length,NumberRange,Regexp
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SearchField, DecimalField, EmailField

# apartir de la clase se puede definir el formulario
class UserForm(Form):
    matricula = StringField('Matricula')
    edad = IntegerField('Edad')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    correo =  EmailField('Correo')
