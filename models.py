from extensions import db
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey
import uuid
from datetime import datetime

# -----------------------
# Staff model
# -----------------------
class Staff(db.Model):
    __tablename__ = 'staff'

    Id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    Name: Mapped[Optional[str]] = mapped_column(db.Text)
    Role: Mapped[Optional[str]] = mapped_column(db.Text)
    Speciality: Mapped[Optional[str]] = mapped_column(db.Text)
    Contact: Mapped[Optional[str]] = mapped_column(db.Text)
    
    __mapper_args__ = {
        'with_polymorphic': '*',
    }


# -----------------------
# Doctor model
# -----------------------
class Doctor(Staff):
    __tablename__ = 'doctor'

    Id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey('staff.Id'), primary_key=True, default=uuid.uuid4)
    LicenseNumber: Mapped[Optional[str]] = mapped_column(db.Text)
    
    __mapper_args__ = {
            'polymorphic_identity': 'doctor',
        }

# -----------------------
# Nurse table
# -----------------------
class Nurse(Staff):
    __tablename__ = 'nurse'

    Id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey('staff.Id'), primary_key=True, default=uuid.uuid4)
    Certification: Mapped[Optional[str]] = mapped_column(db.Text)
    __mapper_args__ = {
            'polymorphic_identity': 'nurse',
    }


# -----------------------
# Shift table
# -----------------------
class Shift(db.Model):
    __tablename__ = 'shift'

    Id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    Id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey('staff.Id'), primary_key=True, default=uuid.uuid4)
    ShiftStart: Mapped[Optional[datetime]] = mapped_column(db.Text)
    ShiftEnd: Mapped[Optional[datetime]] = mapped_column(db.Text)

    staff = relationship('Staff', back_populates='shift')
