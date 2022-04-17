
from flask import Blueprint,render_template,redirect,url_for
from flask_login import current_user, login_required
from project import engine
from sqlalchemy.orm import sessionmaker
from project import db
from project.docenten.forms import GegevensForm, TaalForm, RoostersForm, LesForm
from project.models import Lessen, programmeer_talen, Gebruikers



docenten_blueprint = Blueprint('docenten', __name__, template_folder='templates')




# roosters toevoegen
@docenten_blueprint.route('/roosters', methods=['GET','POST'])
@login_required
def roosters():
    form = RoostersForm()
    if form.validate_on_submit():
    
        nieuwrooster = Lessen.query.filter_by(id=form.lesid.data).first()
        nieuwrooster.docent_id = current_user.id
        nieuwrooster.taal_id = form.taalid.data
        nieuwrooster.start = form.start.data
        nieuwrooster.locatie = form.locatie.data
        db.session.commit()

        return render_template('roosters_wijzigen.html', form=form, methods=['GET','POST'])
    return render_template('roosters_wijzigen.html', form=form, methods=['GET','POST'])

# cursussen toevoegen
@docenten_blueprint.route('/cursussen', methods=['GET','POST'])
@login_required
def cursussen():
    form = LesForm()
    if form.validate_on_submit():
        nieuweles = Lessen(docent_id=current_user.id,taal_id=form.taal.data,start=form.start.data,locatie=form.locatie.data)
        db.session.add(nieuweles)
        db.session.commit()

        return render_template('les_toevoegen.html',form=form,  methods=['GET','POST'])
    return render_template('les_toevoegen.html',form=form, methods=['GET','POST'])

# talen toevoegen
@docenten_blueprint.route('/talen', methods=['GET','POST'])
@login_required
def talen():
    form = TaalForm()
    if form.validate_on_submit():
        nieuwetaal = programmeer_talen(naam=form.taalnaam.data)
        db.session.add(nieuwetaal)
        db.session.commit()

        return render_template('taal_toevoegen.html',form=form, methods=['GET','POST'])
    return render_template('taal_toevoegen.html',form=form, methods=['GET','POST'])


# docentgegevens bewerken
@docenten_blueprint.route('/gegevens', methods=['GET','POST'])
@login_required
def gegevens():
    form = GegevensForm()
    if form.validate_on_submit():

        nieuwegegevens = Gebruikers.query.filter_by(id=current_user.id).first()
        nieuwegegevens.emailadres = form.email.data
        db.session.commit()
        
        return render_template('gegevens_bewerken.html',form=form, methods=['GET','POST'])
    return render_template('gegevens_bewerken.html',form=form, methods=['GET','POST'])
