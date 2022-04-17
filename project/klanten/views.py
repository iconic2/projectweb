from flask import Blueprint,render_template,redirect,url_for
from project import engine
from sqlalchemy.orm import sessionmaker
from project.models import Lessen



klanten_blueprint = Blueprint('klanten', __name__, template_folder='templates')



# roosters bekijken
@klanten_blueprint.route('/roosters', methods=['GET'])
def list():
    lessen = Lessen.query.all()
    print(lessen)
    return render_template('les.html', lessen=lessen)


# aanmelden bij cursus
@klanten_blueprint.route('/inschrijven', methods=['GET'])
def list():
    lessen = Lessen.query.all()
    print(lessen)
    return render_template('les.html', lessen=lessen)

# bekijk alle cursussen
@klanten_blueprint.route('/cursussen', methods=['GET'])
def list():
    lessen = Lessen.query.all()
    print(lessen)
    return render_template('les.html', lessen=lessen)
