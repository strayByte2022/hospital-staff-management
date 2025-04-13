# app.py
from flask import Flask
from shared.extensions import db, migrate
from shared.init import init_staff_blueprint, init_patient_blueprint
from patient_management.models import *
from staff_management.models import *
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)

    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(init_staff_blueprint())
    app.register_blueprint(init_patient_blueprint())
    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
