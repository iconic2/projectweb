
from cgi import test
from pydoc import locate
from tracemalloc import start
from flask import Flask, render_template,redirect, url_for, Blueprint,flash, request, session
from flask_wtf import FlaskForm
from project.forms import  Klantlogin,Docentlogin, LesForm, Registreren 
from project.models import *
from project import app,login_manager,db, engine
from flask_login import login_user, logout_user,login_required, LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@app.route("/")
def index():
    return render_template("home.html")


######### BEGIN REGISTRATIES

@app.route("/registreer",methods=['GET','POST'])
def registreer():
    form = Registreren()

    if form.validate_on_submit():

        # Als email en gebruikersnaam niet bestaan oftewel is None:
        if form.validate_email(form.email) == None and form.validate_username(form.gebruikersnaam) == None:
        
            user = Gebruikers(emailadres=form.email.data,gebruikersnaam=form.gebruikersnaam.data,wachtwoord=form.wachtwoord.data,is_docent=0)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('inloggen'))


        
        
    return render_template('registreer.html',form=form)


@app.route("/docent/registreer",methods=['GET','POST'])
def registreerdocent():
    form = Registreren()

    if form.validate_on_submit():
       
        # Als email,gebruikersnaam niet bestaan oftewel is None:
        if form.validate_email(form.email) == None and form.validate_username(form.gebruikersnaam) == None:
            user = Gebruikers(emailadres=form.email.data,gebruikersnaam=form.gebruikersnaam.data,wachtwoord=form.wachtwoord.data,is_docent=1)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('logindocent'))
        else:
            return render_template('registreer.html',form=form)
    return render_template('registreer.html',form=form)


######### EINDE REGISTRATIES



######### BEGIN LOGINS


@app.route("/inloggen", methods=["GET","POST"])
def inloggen():
    """
    De login voor klanten
    """
    form = Klantlogin()
    
    if form.validate_on_submit():
        
        # voor alleen de klanten checken of gebruiker bestaat:
        user = Gebruikers.query.filter_by(emailadres=form.email.data).first()
        
        if user is not None and user.check_password(form.wachtwoord.data):
        
            login_user(user)
            return redirect(url_for("leerlingen"))

        else:
            return redirect(url_for("inloggen"))

    return render_template('login.html',form=form)


@app.route("/docent/inloggen", methods=["GET","POST"])
def logindocent():
    """
    De login voor docenten
    """
    
    Session = sessionmaker(bind=engine)
    session = Session()

    form = Docentlogin()
    if form.validate_on_submit():
       # bestaat de gebruiker?:
       user = Gebruikers.query.filter_by(emailadres=form.email.data).first()

       # gekozen om te kijken of de gebruiker ook een docent is
       # deze query bekijkt wat de waarde is van de kolom is_docent bij het ingevuld emailadres.
       docent = session.query(Gebruikers.is_docent).filter(Gebruikers.emailadres==form.email.data).first()

       # converteren naar lijst, zodat we makkelijk een element kunnen selecteren. :
       if docent != None:
        docent = [value for value in docent]
       
       # kijken of het wachtwoord overeenkomt, gebruiker niet leeg is en de gebruiker een docent is.
       if user is not None and user.check_password(form.wachtwoord.data) and docent[0] != 0:
            login_user(user)
       
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('docenten')
                return redirect(next)
         
       flash('Of u bent geen docent, of uw inloggegevens zijn onjuist.')
    return render_template('docentlogin.html',form=form)

######### EINDE LOGINS


@app.route("/uitloggen")
@login_required
def uitloggen():
    logout_user()
    flash('U bent uitgelogd!')
    return redirect(url_for('index'))
# leerlingen zullen alle acties die ze mogen doen, op deze pagina kunnen doen.


@app.route("/leerlingen")
@login_required
def leerlingen():

    return render_template('cursisthome.html')


@app.route("/docenten")
@login_required
def docenten():
    return render_template('docenthome.html')


# leerlingen zullen alle acties die ze mogen doen, op deze pagina kunnen doen.













    






# Alleen runnen als de code in dit bestand direct is uitgevoerd en niet als module is aangeroepen:
if __name__ == "__main__":
    app.run(debug=True)