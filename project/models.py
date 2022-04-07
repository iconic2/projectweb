




# !!! NOG NIET AF!!!





##################################################################################3

# In dit bestand maken we de tabellen aan in de database 

from flask_sqlalchemy import SQLAlchemy, String, Integer, VARCHAR,date
from flask import Flask


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database-test.sqlite'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


'''
We hebben de tabellen:

- Docenten
- Klanten
- klant_lessen (Tussentabel)
- lessen
- programmeertalen


'''
class Docenten(db.Model):
    __tablename__ = 'docenten'
    id = db.Column(db.Integer, primary_key=True)#AUTOINCREMENT NOG TOEVOEGEN
    emailadres = db.Column(db.VARCHAR(50))
    gebruikersnaam = db.Column(db.VARCHAR(25))#UNIQUE
    gebruikersnaam = db.Column(db.VARCHAR(128))#UNIQUE


class Klanten(db.Model):
    __tablename__ = 'klanten'
    id = db.Column(db.Integer, primary_key=True)#AUTOINCREMENT NOG TOEVOEGEN
    emailadres = db.Column(db.VARCHAR(50))
    gebruikersnaam = db.Column(db.VARCHAR(25))#UNIQUE
    gebruikersnaam = db.Column(db.VARCHAR(128))#UNIQUE


class Lessen(db.Model):
    __tablename__ = 'lessen'
    id = db.Column(db.Integer, primary_key=True)#AUTOINCREMENT NOG TOEVOEGEN
    docent_id = db.Column(db.Integer, db.ForeignKey('docent.id'))
    taal_id = db.Column(db.Integer,db.ForeignKey('taal.id'))
    start = db.Column(db.date)
    locatie = db.Column(db.varchar(20))# TOEVOEGEN MET UNIQUE
# Database connectie

class programmeer_talen(db.Model):
    __tablename__ = 'talen'
    id = db.Column(db.Integer, primary_key=True)#AUTOINCREMENT NOG TOEVOEGEN
    naam = db.Column(db.VARCHAR(20))
    #UNIQUE TOEVOEGEN

class Klant_Lessen(db.Model):
    __tablename__ = 'klant_lessen'
    k_id = db.Column(db.Integer,db.ForeignKey('klant.id') primary_key=True) #AUTOINCREMENT NOG TOEVOEGEN
    L_id = db.Column(db.Integer,db.ForeignKey('lessen.id'), primary_key=True )#AUTOINCREMENT NOG TOEVOEGEN
  
