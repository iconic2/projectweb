from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
            PasswordField, DateField, EmailField,IntegerField)
#from wtforms.validators import DataRequired, email_validator as email
from wtforms.validators import data_required,DataRequired, email, EqualTo, ValidationError
from project.models import Gebruikers
from flask import flash


class RoostersForm(FlaskForm):
    lesid = IntegerField("Lesid", validators=[DataRequired()])
    taalid = IntegerField("Taalid", validators=[DataRequired()])
    start = StringField("Start", validators=[DataRequired()])
    locatie = StringField("Locatie", validators=[DataRequired()])
    submit = SubmitField('Versturen')
    
class LesForm(FlaskForm): #hierbij gebruiken we het docentid van de Docent die is ingelogd
    taal = IntegerField("Taal id", validators=[DataRequired()])
    start = DateField("Datum", validators=[DataRequired()])
    locatie = StringField("Locatie", default="Online")
    submit = SubmitField('Versturen')

class TaalForm(FlaskForm):
    taalnaam = StringField("Taal", validators=[DataRequired()])
    submit = SubmitField('Versturen')

class GegevensForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField('Versturen')
