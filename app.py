from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, make_response  # Import jsonify and make_response
import os

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)

# Import and register blueprints
from views import staff_views
app.register_blueprint(staff_views.staff_bp)

# Create database tables within the app context
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)