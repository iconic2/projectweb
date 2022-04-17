
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from project import login_manager,db,app

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import UniqueConstraint



# haal id op van gebruiker
@login_manager.user_loader
def load_user(user_id):
    return Gebruikers.query.get(user_id)



class Gebruikers(db.Model,UserMixin):
    __tablename__ = 'gebruikers'
    id = db.Column(db.Integer, primary_key=True)
    emailadres = db.Column(db.VARCHAR(50))
    gebruikersnaam = db.Column(db.VARCHAR(25))
    wachtwoord = db.Column(db.VARCHAR(128))
    is_docent = db.Column(db.Integer, default=0)

    def __init__(self, emailadres,gebruikersnaam,wachtwoord,is_docent):
        self.emailadres = emailadres
        self.gebruikersnaam = gebruikersnaam
        self.wachtwoord = generate_password_hash(wachtwoord)
        self.is_docent = is_docent

    def check_password(self,password):
        return check_password_hash(self.wachtwoord, password)


class Lessen(db.Model,UserMixin):
    __tablename__ = 'lessen'
    id = db.Column(db.Integer, primary_key=True)
    docent_id = db.Column(db.Integer, db.ForeignKey('gebruikers.id'))
    taal_id = db.Column(db.Integer,db.ForeignKey('talen.id'))
    start = db.Column(db.VARCHAR(20))
    locatie = db.Column(db.VARCHAR(20))

    def __repr__(self):
        return f"Les {self.id} gegeven door {self.docent_id} begint om {self.start} in {self.locatie}"
# Database connectie


class gebruikers_Lessen(db.Model,UserMixin):
    __tablename__ = 'gebruikers_lessen'
    g_id = db.Column(db.Integer,db.ForeignKey('gebruikers.id'), primary_key=True) 
    l_id = db.Column(db.Integer,db.ForeignKey('lessen.id'), primary_key=True)


class programmeer_talen(db.Model,UserMixin):
    __tablename__ = 'talen'
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.VARCHAR(20))
    UniqueConstraint('naam','id',name='uc1')
    

db.create_all()