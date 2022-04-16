
from pydoc import locate
from tracemalloc import start
from flask import Flask, render_template,redirect, url_for, Blueprint,flash
from flask_wtf import FlaskForm
from project.forms import GegevensForm, Klantlogin,Docentlogin, LesForm, Registreren, RegistrerenDocent, RoostersForm, TaalForm
from project.models import *
from project import app,login_manager,db
from flask_login import login_user, logout_user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#klanten_blueprint = Blueprint('Klanten', __name__,template_folder='templates')
#docenten_blueprint = Blueprint('Docenten', __name__,template_folder='templates')

#app.register_blueprint(klanten_blueprint,url_prefix="/cursist")
#app.register_blueprint(docenten_blueprint,url_prefix="/docenten")


@app.route("/")
def index():
    return render_template("home.html")



@app.route("/registreer",methods=['GET','POST'])
def registreer():
    form = Registreren()
    #print(form.validate_email(form.email))
    #print(form.validate_username(form.gebruikersnaam))
    if form.validate_on_submit():

        # Als email en gebruikersnaam niet bestaan oftewel is None:
        if form.validate_email(form.email) == None and form.validate_username(form.gebruikersnaam) == None:
        
            user = Gebruikers(emailadres=form.email.data,gebruikersnaam=form.gebruikersnaam.data,wachtwoord=form.wachtwoord.data,is_docent=0)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        
        return render_template('registreer.html',form=form)
    return render_template('registreer.html',form=form)


@app.route("/docent/registreer",methods=['GET','POST'])
def registreerdocent():
    form = RegistrerenDocent()
    #print(form.validate_email(form.email))
    #print(form.validate_username(form.gebruikersnaam))
    if form.validate_on_submit():

        # Als email en gebruikersnaam niet bestaan oftewel is None:
        if form.validate_email(form.email) == None and form.validate_username(form.gebruikersnaam) == None:
        
            user = Gebruikers(emailadres=form.email.data,gebruikersnaam=form.gebruikersnaam.data,wachtwoord=form.wachtwoord.data,is_docent=1)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('logindocent'))
        
        return render_template('registreer.html',form=form)
    return render_template('registreer.html',form=form)

@app.route("/inloggen", methods=["GET","POST"])
def login():
    """
    De login voor klanten
    """
    form = Klantlogin()
    if form.validate_on_submit():
       # voor alleen de klanten checken of gebruiker bestaat:
       user = Gebruikers.query.filter_by(emailadres=form.email.data).first()
       if user.check_password(form.wachtwoord.data) and user is not None:
          login_user(user)
          return redirect(url_for("leerlingen"))
      
    return render_template('login.html',form=form)

@app.route("/docent/inloggen", methods=["GET","POST"])
def logindocent():
    """
    De login voor docenten
    """
    engine = create_engine('sqlite:///project/database.sqlite')

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
       docent = [value for value in docent]
       
       # kijken of het wachtwoord overeenkomt, gebruiker niet leeg is en de gebruiker een docent is.
       if user.check_password(form.wachtwoord.data) and user is not None and docent[0] != 0:
          login_user(user)
          return 'WELKOM DOCENT'
       flash('Of je bent geen docent, of je inloggegevens zijn onjuist.')
    return render_template('docentlogin.html',form=form)


@app.route("/leerlingen")
def leerlingen():
    return render_template("leerlingen.html")
# leerlingen zullen alle acties die ze mogen doen, op deze pagina kunnen doen.


@app.route("/docenten")
def docenten():
    return render_template("docenten.html")

@app.route("/cursussen")
def cursussen():
    return render_template("cursussen.html")


######## HIERONDER DE VIEWS ############
@app.route("/roosters_wijzigen")
def roosters_wijzigen():
    form = RoostersForm()

    if form.validate_on_submit():       

        nieuwrooster = Lessen.query.filter_by(id=form.lesid.data).first()
        nieuwrooster.docent_id = session.query(Gebruikers.id)
        nieuwrooster.taal_id = form.taalid.data
        nieuwrooster.start = form.start.data
        nieuwrooster.locatie = form.locatie.data
        db.session.commit()
        
        return render_template('roosters_wijzigen.html',form=form)
    return render_template('roosters_wijzigen.html',form=form)

@app.route("/les_toevoegen")
def les_toevoegen():
    form = LesForm()

    if form.validate_on_submit():

        nieuweles = Lessen(docent_id=session.query(Gebruikers.id),taal_id=form.taal.data,start=form.start.data,locatie=form.locatie.data)
        db.session.add(nieuweles)
        db.session.commit()
        
        return render_template('les_toevoegen.html',form=form)
    return render_template('les_toevoegen.html',form=form)


@app.route("/taal_toevoegen")
def taal_toevoegen():
    form = TaalForm()

    if form.validate_on_submit():
        
        nieuwetaal = programmeer_talen(naam=form.taalnaam.data)
        db.session.add(nieuwetaal)
        db.session.commit()
        
        return render_template('taal_toevoegen.html',form=form)
    return render_template('taal_toevoegen.html',form=form)

@app.route("/gegevens_bewerken")
def gegevens_bewerken():
    form = GegevensForm()

    if form.validate_on_submit():
        
        nieuwegegevens = Gebruikers.query.filter_by(id=session.query(Gebruikers.id)).first()
        nieuwegegevens.emailadres = form.email.data
        db.session.commit()
        
        return render_template('gegevens_bewerken.html',form=form)
    return render_template('gegevens_bewerken.html',form=form)


# Alleen runnen als de code in dit bestand direct is uitgevoerd en niet als module is aangeroepen:
if __name__ == "__main__":
    app.run(debug=True)
