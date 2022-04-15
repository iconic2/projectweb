from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__,template_folder="templates")

# SECRET KEY VOOR PREVENTIE CSRF
app.config['SECRET_KEY']='ADFADSFAHFKA&&&&*D11'

# AANGEVEN WAAR DATABASE STAAT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


login_manager = LoginManager()
login_manager.init_app(app)
#login_manager.login_view("login")
#login_manager.login_message = "U moet eerst inloggen."

db = SQLAlchemy(app)
