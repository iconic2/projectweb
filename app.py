from flask import Flask, render_template,redirect, url_for
from flask_wtf import FlaskForm
from project.forms import klantlogin
from project.models import *
from project import app,login_manager,db
from flask_login import login_user, logout_user



@app.route("/")
def index():
    return render_template("home.html")

@app.route("/register")
def registreer():

    return render_template('home.html')


@app.route("/inloggen", methods=["GET","POST"])
def login():
    form = klantlogin()
    if form.validate_on_submit():
       user = Klanten.query.filter_by(emailadres=form.email.data).first()
       print('USER IS' , user)
       if user.check_password(form.wachtwoord.data) and user is not None:
          login_user(user)
          print('JAAAAAAAAAAAA')
       return redirect(url_for("registreer"))
    return render_template('login.html',form=form)





@app.route("/leerlingen")
def leerlingen():
    return render_template("leerlingen.html")
# leerlingen zullen alle acties die ze mogen doen, op deze pagina kunnen doen.


@app.route("/docenten")
def docenten():
    return render_template("docenten.html")




######## HIERONDER DE VIEWS ############
@app.route("/roosters_wijzigen")
def roosters_wijzigen():
    return render_template('roosters_wijzigen.html')

@app.route("/les_toevoegen")
def les_toevoegen():
    return render_template('les_toevoegen.html')

@app.route("/taal_toevoegen")
def taal_toevoegen():
    return render_template('taal_toevoegen.html')

@app.route("/gegevens_bewerken")
def gegevens_bewerken():
    return render_template('gegevens_bewerken.html')


# Alleen runnen als de code in dit bestand direct is uitgevoerd en niet als module is aangeroepen:
if __name__ == "__main__":
    app.run(debug=True)