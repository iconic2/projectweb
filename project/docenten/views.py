from flask import Blueprint,render_template,redirect,url_for
from project import engine
from sqlalchemy.orm import sessionmaker
from project.models import Lessen



docenten_blueprint = Blueprint('docenten', __name__, template_folder='templates')



# roosters toevoegen
@docenten_blueprint.route('/roosters', methods=['GET'])
def list():
    Session = sessionmaker(bind=engine)
    session = Session()

    lessen = Lessen.query.all()

    return render_template('les.html', lessen=lessen)


# cursussen toevoegen
@docenten_blueprint.route('/cursussen', methods=['GET'])
def list():
    Session = sessionmaker(bind=engine)
    session = Session()

    lessen = Lessen.query.all()

    return render_template('les.html', lessen=lessen)

# talen toevoegen
@docenten_blueprint.route('/talen', methods=['GET'])
def list():
    Session = sessionmaker(bind=engine)
    session = Session()

    lessen = Lessen.query.all()

    return render_template('les.html', lessen=lessen)


# docentgegevens bewerken
@docenten_blueprint.route('/gegevens', methods=['GET'])
def list():
    Session = sessionmaker(bind=engine)
    session = Session()

    lessen = Lessen.query.all()

    return render_template('les.html', lessen=lessen)