# app.py
from flask import Flask
from extensions import db, migrate
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from controllers.staff_controller import staff_controller
    app.register_blueprint(staff_controller)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
