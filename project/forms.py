from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import data_required, email, EqualTo, ValidationError
from project.models import Gebruikers
from flask import flash


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