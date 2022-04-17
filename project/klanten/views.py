from flask import Blueprint,render_template,redirect,url_for
from project import engine
from sqlalchemy.orm import sessionmaker
from project.models import Lessen



klanten_blueprint = Blueprint('klanten', __name__, template_folder='templates')



# roosters bekijken
@klanten_blueprint.route('/roosters', methods=['GET'])
def roosters():
    roosters = Lessen.query.all()
    print(roosters)
    return render_template('les.html', roosters=roosters)


# aanmelden bij cursus
@klanten_blueprint.route('/inschrijven', methods=['GET'])
def inschrijven():
    inschrijven = Lessen.query.all()
    print(inschrijven)
    return render_template('les.html', inschrijven=inschrijven)

# bekijk alle cursussen
@klanten_blueprint.route('/cursussen', methods=['GET'])
def cursussen():
    cursussen = Lessen.query.all()
    print(cursussen)
    return render_template('les.html', cursussen=cursussen)
