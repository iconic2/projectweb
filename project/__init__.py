from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_login import LoginManager








app = Flask(__name__,template_folder="templates")

# SECRET KEY VOOR PREVENTIE CSRF
app.config['SECRET_KEY']='ADFADSFAHFKA&&&&*D11'



# AANGEVEN WAAR DATABASE STAAT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine('sqlite:///project/database.sqlite')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "U moet eerst inloggen."
login_manager.login_view = "inloggen"

db = SQLAlchemy(app)

from project.klanten.views import klanten_blueprint
app.register_blueprint(klanten_blueprint,url_prefix="/cursisten")

from project.docenten.views import docenten_blueprint
app.register_blueprint(docenten_blueprint,url_prefix="/docenten")