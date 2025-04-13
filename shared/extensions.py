# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

'''
Here is an issue without this file

app.py ➡ imports models.py (for Staff)
models.py ➡ needs db from app.py
staff_repository.py ➡ also imports db from app.py

We need to implement factory pattern to ensure they all use the same db 

'''