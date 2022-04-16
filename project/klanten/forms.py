from flask import Blueprint,render_template,redirect,url_for
from project import db
from project.models import Lessen



klanten_blueprint = Blueprint('klanten', __name__, template_folder='templates')


@klanten_blueprint.route('/lessen', methods=['GET'])
def list():
    lessen = Lessen.query.all()
    print(lessen)
    return render_template('les.html', lessen=lessen)