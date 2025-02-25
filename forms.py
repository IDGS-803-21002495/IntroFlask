from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo,Length,NumberRange,Regexp
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SearchField, DecimalField, EmailField

from wtforms import validators

# apartir de la clase se puede definir el formulario
class UserForm(Form):
    matricula = StringField('Matricula',[
        # validar que sea un campo requerido
        validators.DataRequired("Este campo es requerido"),
        # validar la longitud de un campo (entre 2 y 10)
        #validators.Length(min=2, max=10, message="La matricula debe tener entres 2 y 10 caracteres")
    ])
    edad = IntegerField('Edad',[
        validators.DataRequired("Este campo es requerido")
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired("Este campo es requerido")
    ])
    apellidos = StringField('Apellidos',[
        validators.DataRequired("Este campo es requerido")
    ])
    correo =  EmailField('Correo',[
        validators.Email(message="Ingrese un correo valido")
    ])
