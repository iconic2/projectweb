from distutils.log import debug
from flask import Flask, render_template
from flask_wtf import FlaskForm
#from forms.py import LoginForm

app = Flask(__name__, template_folder="templates")




@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login")
def login():
    #form = LoginForm()
    #f form.validat_on_submit():
    return render_template('login.html')


@app.route("/leerlingen")
def leerlingen():
    return render_template("leerlingen.html")
# leerlingen zullen alle acties die ze mogen doen, op deze pagina kunnen doen.


@app.route("/docenten")
def docenten():
    return render_template("docenten.html")

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



if __name__ == "__main__":
    app.run(debug=True)
