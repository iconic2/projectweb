from tracemalloc import start
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
            PasswordField, DateField, EmailField,IntegerField)
#from wtforms.validators import DataRequired, email_validator as email
from wtforms.validators import data_required,DataRequired, email, EqualTo, ValidationError
from project.models import Gebruikers
from flask import flash




class RoostersForm(FlaskForm):
    lesid = IntegerField("Lesid", validators=[DataRequired()])
    taalid = StringField("Taalid", validators=[DataRequired()])
    start = StringField("Start", validators=[DataRequired()])
    locatie = StringField("Locatie", validators=[DataRequired()])
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
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField('Versturen')

class InschrijfForm(FlaskForm):
    voornaam = StringField("Voornaam", validators=[DataRequired()])
    submit = SubmitField('Versturen')


class Klantlogin(FlaskForm):
    email = StringField('Voer hier uw emailadres in',validators=[data_required(),email()])
    wachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    submit = SubmitField('Inloggen')

class Docentlogin(FlaskForm):
    email = StringField('Voer hier uw emailadres in',validators=[data_required(),email()])
    wachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    submit = SubmitField('Inloggen')


class Registreren(FlaskForm):
    email = StringField('Voer hier uw emailadres in',validators=[data_required(),email()])
    gebruikersnaam = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    wachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required(),EqualTo('herhaalwachtwoord', message='Wachtwoorden moeten overeenkomen')])
    herhaalwachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    submit = SubmitField('Registreren')

    def validate_email(self, field):
        if Gebruikers.query.filter_by(emailadres=field.data).first():
            flash('Deze email bestaat al!')
            return False
    
    def validate_username(self, field):
        if Gebruikers.query.filter_by(gebruikersnaam=field.data).first():
            flash('Deze gebruikersnaam bestaat al!')
            return False

class RegistrerenDocent(FlaskForm):
    email = StringField('Voer hier uw emailadres in',validators=[data_required(),email()])
    gebruikersnaam = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    wachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required(),EqualTo('herhaalwachtwoord', message='Wachtwoorden moeten overeenkomen')])
    herhaalwachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    submit = SubmitField('Registreren')

    def validate_email(self, field):
        if Gebruikers.query.filter_by(emailadres=field.data,is_docent=1).first():
            flash('Deze email bestaat al!')
            return False
    
    def validate_username(self, field):
        if Gebruikers.query.filter_by(gebruikersnaam=field.data,is_docent=1).first():
            flash('Deze gebruikersnaam bestaat al!')
            return False
