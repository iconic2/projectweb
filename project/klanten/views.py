from distutils.ccompiler import gen_lib_options
from operator import le
from flask import Blueprint,render_template,redirect,url_for,flash
from project import engine,db
from sqlalchemy.orm import sessionmaker
from project.models import Lessen,programmeer_talen, Gebruikers, gebruikers_Lessen
from flask_login import login_required,current_user
from project.klanten.forms import Inschrijven



klanten_blueprint = Blueprint('klanten', __name__, template_folder='templates')


@klanten_blueprint.route('/cursussen', methods=['GET'])
@login_required
def cursussen():
    """
    Geeft ALLE beschikbare lessen terug
    
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    lijst = []
   # Bron: https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_joins.htm
    for lessen,talen,docenten in session.query(Lessen, programmeer_talen,Gebruikers).filter(Lessen.taal_id == programmeer_talen.id, Lessen.docent_id == Gebruikers.id).all():
        lijst += [[lessen.id,talen.naam,docenten.gebruikersnaam,lessen.start,lessen.locatie]]

        
    print(lijst)
    return render_template('les.html' , lijst=lijst)



@klanten_blueprint.route('/roosters', methods=['GET'])
@login_required
def roosters():
    """
    Geeft informatie terug over bij welke cursus(sen) de gebruiker is ingeschreven.
    """
    # id pakken van huidige gebruiker:

    Session = sessionmaker(bind=engine)
    session = Session()

    # wie is de huidige gebruiker?
    gebruiker = current_user.id
    lijst = []

    for les,gebruiker_les,gebruikers,talen in session.query(Lessen, gebruikers_Lessen,Gebruikers, programmeer_talen).filter(gebruikers_Lessen.g_id == Gebruikers.id, gebruikers_Lessen.l_id == Lessen.id, Lessen.taal_id == programmeer_talen.id, Gebruikers.id == gebruiker).all():
    
        lijst += [[les.id,les.start,les.locatie,talen.naam]]

    return render_template('roosters.html', lijst=lijst)
        




@klanten_blueprint.route('/inschrijven', methods=['GET', 'POST'])
@login_required
def inschrijven():
    gebruiker = current_user.id

    form = Inschrijven()
    if form.validate_on_submit():
    
        inschrijven = gebruikers_Lessen(l_id=form.lesid.data,g_id=current_user.id)
        db.session.add(inschrijven)
        db.session.commit()

        flash('Je bent ingeschreven!')
    return render_template('inschrijven.html', form=form)
    
    
    
    