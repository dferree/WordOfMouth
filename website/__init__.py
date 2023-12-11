from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

DB_NAME = "database.db"
INSTANCE_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')

# create the python app
def create_app(instance_path=None):
    app = Flask(__name__, instance_path=instance_path)
    # configure the secret key (usuallty would be somethign secretive)
    app.config['SECRET_KEY'] = 'secretkey'
    # direct the database location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.instance_path, DB_NAME)}'
    # initialise the database
    db.init_app(app)
    
    
    from .views import views
    from .auth import auth
    
    # build url prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note, Activity, Review
      
    # create database within flask app context  
    with app.app_context():
        create_database(app)
        
    login_manager = LoginManager()
    # direct user to login page if not logged in
    login_manager.login_view = 'auth.login'
    # tell login manager which app we are using
    login_manager.init_app(app)
    
    # use function below to load user
    @login_manager.user_loader
    def load_user(id):
        # user.query.get automatically looks for the primary key
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists(os.path.join(app.instance_path, DB_NAME)):
        db.create_all()
        print('Created Database!')
    else:
        print('Database exists.')