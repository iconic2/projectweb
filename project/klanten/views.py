from flask import Blueprint,render_template,redirect,url_for
from project import engine
from sqlalchemy.orm import sessionmaker
from project.models import Lessen



klanten_blueprint = Blueprint('klanten', __name__, template_folder='templates')


@klanten_blueprint.route('/lessen', methods=['GET'])
def list():
    Session = sessionmaker(bind=engine)
    session = Session()

    lessen = Lessen.query.all()

    return render_template('les.html', lessen=lessen)