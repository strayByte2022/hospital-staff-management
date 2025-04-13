from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey
import uuid
from datetime import datetime
from shared.base_model import BaseModel, db
# -----------------------
# Staff model
# -----------------------
class Staff(BaseModel):
    __tablename__ = 'staff'

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[Optional[str]] = mapped_column(db.Text)
    role: Mapped[Optional[str]] = mapped_column(db.Text)
    specialty: Mapped[Optional[str]] = mapped_column(db.Text)
    contact: Mapped[Optional[str]] = mapped_column(db.Text)
    
    __mapper_args__ = {
        'with_polymorphic': '*',
    }
    
    shifts = relationship('Shift', back_populates='staff')
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'role': self.role,
            'specialty': self.specialty,
            'contact': self.contact
        }


# -----------------------
# Doctor model
# -----------------------
class Doctor(Staff):
    __tablename__ = 'doctor'

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey('staff.id'), primary_key=True, default=uuid.uuid4)
    license_number: Mapped[Optional[str]] = mapped_column(db.Text)
    
    __mapper_args__ = {
            'polymorphic_identity': 'doctor',
        }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'role': self.role,
            'specialty': self.specialty,
            'contact': self.contact,
            'license_number': self.license_number
        }

# -----------------------
# Nurse table
# -----------------------
class Nurse(Staff):
    __tablename__ = 'nurse'

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey('staff.id'), primary_key=True, default=uuid.uuid4)
    certification: Mapped[Optional[str]] = mapped_column(db.Text)
    __mapper_args__ = {
            'polymorphic_identity': 'nurse',
    }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'role': self.role,
            'specialty': self.specialty,
            'contact': self.contact,
            'certification': self.certification
        }

# -----------------------
# Shift table
# -----------------------
class Shift(BaseModel):
    __tablename__ = 'shift'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    staff_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey('staff.id'), primary_key=True, default=uuid.uuid4)
    shift_start: Mapped[Optional[datetime]] = mapped_column(db.Text)
    shift_end: Mapped[Optional[datetime]] = mapped_column(db.Text)

    staff = relationship('Staff', back_populates='shifts')
    
    def to_dict(self):
        return {
            'id': self.id,
            'staff_id': str(self.staff_id),
            'shift_start': self.shift_start,
            'shift_end': self.shift_end
        }
    