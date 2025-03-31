from app import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))  # Foreign Key
    # ... other staff fields ...

    department = db.relationship('Department', backref=db.backref('staff_members', lazy=True))  # Relationship

    def __repr__(self):
        return f'<Staff {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'department_id': self.department_id,
            # ... other fields ...
        }

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Department {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }