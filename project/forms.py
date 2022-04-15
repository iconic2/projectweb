from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import data_required, email

class klantlogin(FlaskForm):
    email = StringField('Voer hier uw emailadres in',validators=[data_required(),email()])
    wachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    submit = SubmitField('Inloggen')

class docentlogin(FlaskForm):
    email = StringField('Voer hier uw emailadres in',validators=[data_required(),email()])
    wachtwoord = StringField('Voer hier uw wachtwoord in', validators=[data_required()])
    submit = SubmitField('Inloggen')
