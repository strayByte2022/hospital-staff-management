# 🏥 Hospital Staff Management – Flask Backend

This project follows a clean monolithic architecture using Flask, SQLAlchemy, and Alembic. This document explains how to add new features (e.g., models, endpoints, services) the proper way.

> [!TIP]
> Document is generated by AI. Be advised!
---

## 🛠 Tech Stack

- Flask (app factory pattern)
- Flask-SQLAlchemy
- Flask-Migrate (Alembic)
- Service/Repository architecture
- RESTful API structure (JSON only)

---

## 🯩 Project Structure

```
/controllers         # API endpoint handlers (controllers)
/services            # Business logic layer
/repositories        # Data access logic (repositories)
/models.py           # SQLAlchemy models
/extensions.py       # Flask extensions like db
/app.py              # App factory + entry point
```

---

## ✨ Adding a New Feature

Let’s say you want to add a new entity: `Patient`.

### 1. 🧱 Define Model in `models.py`

```python
class Patient(db.Model):
    __tablename__ = 'patient'

    Id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(db.String(100))
    Age: Mapped[int] = mapped_column(db.Integer)
    Gender: Mapped[str] = mapped_column(db.String(10))
```

---

### 2. 🏗 Run Alembic Migration

```bash
flask db migrate -m "Add patient table"
flask db upgrade
```

> 🔥 This creates and applies the migration script for the new model.

---

### 3. 🏦 Create Repository

In `repositories/patient_repository.py`:

```python
class PatientRepository:
    def get_all(self): ...
    def get_by_id(self, patient_id): ...
    def add(self, patient): ...
    def update(self, patient): ...
    def delete(self, patient_id): ...
```

---

### 4. 🧠 Create Service

In `services/patient_service.py`:

```python
class PatientService:
    def __init__(self, repository): ...
    def list_patients(self): ...
    def get_patient(self, id): ...
    def create_patient(self, patient): ...
    def edit_patient(self, patient): ...
    def remove_patient(self, id): ...
```

---

### 5. 🌐 Add Controller

In `controllers/patient_controller.py`:

```python
@bp.route('/api/patients')
def get_patients():
    return jsonify(patient_service.list_patients())
```

Then register the blueprint in `app.py`:

```python
from controllers.patient_controller import patient_controller
app.register_blueprint(patient_controller)
```

---

### 🧪 Testing Locally

```bash
flask run
# Test via Postman, curl, or Swagger if enabled
```

---

## ✅ Summary Checklist

- [ ] Add model in `models.py`
- [ ] Run `flask db migrate && flask db upgrade`
- [ ] Create repository
- [ ] Create service
- [ ] Create controller + route
- [ ] Register blueprint
- [ ] Test it!

---

## 🧼 Useful Commands

```bash
flask db migrate -m "Your message"
flask db upgrade
flask db downgrade
flask db current
```

---

## ❤️ Tips

- Keep routes in `controllers/`, logic in `services/`, and DB queries in `repositories/`
- Never edit the database manually. Always use Alembic migrations.
- Use `Mapped[...]` + `mapped_column()` for models to stay future-proof.

