from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import data_required, email, EqualTo, ValidationError, DataRequired
from project.models import Gebruikers
from flask import flash


class Klantlogin(FlaskForm):
    email = StringField('Voer hier uw emailadres in',validators=[data_required(),email()])
    wachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    submit = SubmitField('Inloggen')

class Docentlogin(FlaskForm):
    email = StringField('Voer hier uw emailadres in',validators=[data_required(),email()])
    wachtwoord = StringField('Voer hier uw wachtwoords in', validators=[data_required()])
    submit = SubmitField('Inloggen')


# registreren van cursisten en docenten:
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
        

# Toevoegen van lessen:
class LesForm(FlaskForm): #hierbij gebruiken we het docentid van de Docent die is ingelogd
    taal = StringField("Taal", validators=[DataRequired()])
    start = StringField("Datum", validators=[DataRequired()])
    locatie = StringField("Locatie", default="Online")
    submit = SubmitField('Versturen')
