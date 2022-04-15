from email.policy import default
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
            PasswordField, DateField, EmailField)
from wtforms.validators import DataRequired

class RoostersForm(FlaskForm):
    voornaam = StringField("Voornaam", validators=[DataRequired()])
    submit = SubmitField('Versturen')
    
class LesForm(FlaskForm): #hierbij gebruiken we het docentid van de Docent die is ingelogd
    taal = StringField("Taal", validators=[DataRequired()])
    start = DateField("Datum", validators=[DataRequired()])
    locatie = StringField("Locatie", default="Online")
    submit = SubmitField('Versturen')

class TaalForm(FlaskForm):
    taalnaam = StringField("Taal", validators=[DataRequired()])
    submit = SubmitField('Versturen')

class GegevensForm(FlaskForm):
    email = StringField("Voornaam", validators=[DataRequired()])
    submit = SubmitField('Versturen')

class InschrijfForm(FlaskForm):
    voornaam = StringField("Voornaam", validators=[DataRequired()])
    submit = SubmitField('Versturen')

