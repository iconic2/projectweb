
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from project import login_manager,db,app
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


# haal id op van gebruiker
@login_manager.user_loader
def load_user(user_id):
    return Gebruikers.query.get(user_id)



class Gebruikers(db.Model,UserMixin):
    __tablename__ = 'gebruikers'
    id = db.Column(db.Integer, primary_key=True)#AUTOINCREMENT NOG TOEVOEGEN
    emailadres = db.Column(db.VARCHAR(50))
    gebruikersnaam = db.Column(db.VARCHAR(25))#UNIQUE
    wachtwoord = db.Column(db.VARCHAR(128))#UNIQUE
    is_docent = db.Column(db.Integer, default=0)#UNIQUE

    def __init__(self, emailadres,gebruikersnaam,wachtwoord,is_docent):
        self.emailadres = emailadres
        self.gebruikersnaam = gebruikersnaam
        self.wachtwoord = generate_password_hash(wachtwoord)
        self.is_docent = is_docent

    def check_password(self,password):
        return check_password_hash(self.wachtwoord, password)




class Lessen(db.Model,UserMixin):
    __tablename__ = 'lessen'
    id = db.Column(db.Integer, primary_key=True)#AUTOINCREMENT NOG TOEVOEGEN
    docent_id = db.Column(db.Integer, db.ForeignKey('gebruikers.id'))
    taal_id = db.Column(db.Integer,db.ForeignKey('talen.id'))
    start = db.Column(db.VARCHAR(20))
    locatie = db.Column(db.VARCHAR(20))# TOEVOEGEN MET UNIQUE
# Database connectie

class programmeer_talen(db.Model,UserMixin):
    __tablename__ = 'talen'
    id = db.Column(db.Integer, primary_key=True)#AUTOINCREMENT NOG TOEVOEGEN
    naam = db.Column(db.VARCHAR(20))
    #UNIQUE TOEVOEGEN

class Klant_Lessen(db.Model,UserMixin):
    __tablename__ = 'klant_lessen'
    k_id = db.Column(db.Integer,db.ForeignKey('gebruikers.id'), primary_key=True) 
    L_id = db.Column(db.Integer,db.ForeignKey('lessen.id'), primary_key=True )#AUTOINCREMENT NOG 


db.create_all()