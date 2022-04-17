from certifi import where
from flask import Blueprint,render_template,redirect,url_for
from project import engine
from sqlalchemy.orm import sessionmaker
from project.docenten.forms import GegevensForm, TaalForm
from project.models import Lessen, programmeer_talen, Gebruikers



docenten_blueprint = Blueprint('docenten', __name__, template_folder='templates')



# roosters toevoegen
@docenten_blueprint.route('/roosters', methods=['post'])
def roosters():
    form = RoostersForm()
    if form.validate_on_submit():
        Session = sessionmaker(bind=engine)
        session = Session()
    
        nieuwrooster = Lessen.query.filter_by(id=form.lesid.data).first()
        nieuwrooster.docent_id = session.query(Gebruikers.id)
        nieuwrooster.taal_id = form.taalid.data
        nieuwrooster.start = form.start.data
        nieuwrooster.locatie = form.locatie.data
        db.session.commit()

        return render_template('roosters_wijzigen.html', form=form)
    return render_template('roosters_wijzigen.html', form=form)

# cursussen toevoegen
@docenten_blueprint.route('/cursussen', methods=['post'])
def cursussen():
    form = LesForm()
    if form.validate_on_submit():
        engine = create_engine('sqlite:///project/database.sqlite')
        Session = sessionmaker(bind=engine)
        session = Session()
        nieuweles = Lessen(docent_id=session.query(Gebruikers.id),taal_id=form.taal.data,start=form.start.data,locatie=form.locatie.data)
        db.session.add(nieuweles)
        db.session.commit()

        return render_template('les_toevoegen.html',form=form)
    return render_template('les_toevoegen.html',form=form)

# talen toevoegen
@docenten_blueprint.route('/talen', methods=['post'])
def talen():
    form = TaalForm()
    if form.validate_on_submit():
        nieuwetaal = programmeer_talen(naam=form.taalnaam.data)
        db.session.add(nieuwetaal)
        db.session.commit()

        return render_template('taal_toevoegen.html',form=form)
    return render_template('taal_toevoegen.html',form=form)


# docentgegevens bewerken
@docenten_blueprint.route('/gegevens', methods=['post'])
def gegevens():
    form = GegevensForm()
    if form.validate_on_submit():

        nieuwegegevens = Gebruikers.query.filter_by(id=session.query(Gebruikers.id)).first()
        nieuwegegevens.emailadres = form.email.data
        db.session.commit()
        
        return render_template('gegevens_bewerken.html',form=form)
    return render_template('gegevens_bewerken.html',form=form)