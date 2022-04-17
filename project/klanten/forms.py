from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
            PasswordField, DateField, EmailField,IntegerField)
#from wtforms.validators import DataRequired, email_validator as email
from wtforms.validators import data_required,DataRequired, email, EqualTo, ValidationError
from project.models import Gebruikers
from flask import flash


class Inschrijven(FlaskForm):
    lesid = IntegerField("Lesid", validators=[DataRequired()])
    submit = SubmitField('Inschrijven')