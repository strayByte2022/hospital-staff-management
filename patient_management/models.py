from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey
import uuid
from datetime import datetime
from shared.base_model import BaseModel, db

# -----------------------
# Patient table
# -----------------------

class Patient(BaseModel):
    __tablename__ = 'patient'
    
    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[Optional[str]] = mapped_column(db.Text)
    age: Mapped[Optional[int]] = mapped_column(db.Integer)
    gender: Mapped[Optional[str]] = mapped_column(db.Text)
    contact: Mapped[Optional[str]] = mapped_column(db.Text)
    address: Mapped[Optional[str]] = mapped_column(db.Text)
    
    medical_history = relationship('MedicalHistory', back_populates='patient')
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'contact': self.contact,
            'address': self.address,
        }
    
# -----------------------
# Medical History table
# -----------------------
class MedicalHistory(BaseModel):
    __tablename__ = 'medical_history'
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    patient_id: Mapped[str] = mapped_column(UUID(as_uuid=True), ForeignKey('patient.id'), primary_key=True, default=uuid.uuid4)
    
    patient = relationship('Patient', back_populates='medical_history')
    diagnosis = relationship('Diagnosis', back_populates='medical_history')
    allergy = relationship('Allergy', back_populates='medical_history')
    test_results = relationship('TestResults', back_populates='medical_history')
    prescription = relationship('Prescription', back_populates='medical_history')
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': str(self.patient_id),
            'diagnosis': [d.to_dict() for d in self.diagnosis],
            'allergy': [a.to_dict() for a in self.allergy],
            'test_results': [tr.tod_ict() for tr in self.test_results],
            'prescription': [p.to_dict() for p in self.prescription],
        }
    
# -----------------------
# Diagnosis table
# -----------------------

class Diagnosis(BaseModel):
    __tablename__ = 'diagnosis'
    
    medical_history_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('medical_history.id'), primary_key=True)
    diagnosis: Mapped[Optional[str]] = mapped_column(db.Text, primary_key=True)
    
    medical_history = relationship('MedicalHistory', back_populates='diagnosis')
    
    def to_dict(self):
        return {
            'medical_history_id': self.medical_history_id,
            'diagnosis': self.diagnosis,
        }
    
# -----------------------
# Allergy table
# -----------------------

class Allergy(BaseModel):
    __tablename__ = 'allergy'
    
    medical_history_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('medical_history.id'), primary_key=True)
    allergy: Mapped[Optional[str]] = mapped_column(db.Text, primary_key=True)
    
    medical_history = relationship('MedicalHistory', back_populates='allergy')
    
    def to_dict(self):
        return {
            'medical_history_id': self.medical_history_id,
            'allergy': self.allergy,
        }
    
# -----------------------
# Test Results table
# -----------------------

class TestResults(BaseModel):
    __tablename__ = 'test_results'
    
    medical_history_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('medical_history.id'), primary_key=True)
    test_id: Mapped[Optional[int]] = mapped_column(db.Text, primary_key=True)
    date: Mapped[Optional[datetime]] = mapped_column(db.DateTime)
    result: Mapped[Optional[str]] = mapped_column(db.Text)
    
    
    medical_history = relationship('MedicalHistory', back_populates='test_results')  
    
    def to_dict(self):
        return {
            'medical_history_id': self.medical_history_id,
            'test_id': self.test_id,
            'date': self.date,
            'result': self.result,
        }
    
# -----------------------
# Prescription table
# -----------------------
class Prescription(BaseModel):
    __tablename__ = 'prescription'
    
    medical_history_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('medical_history.id'), primary_key=True)
    prescription_id: Mapped[Optional[int]] = mapped_column(db.Text, primary_key=True)
    medication: Mapped[Optional[str]] = mapped_column(db.Text)
    dosage: Mapped[Optional[str]] = mapped_column(db.Text)
    
    medical_history = relationship('MedicalHistory', back_populates='prescription')  
    
    def to_dict(self):
        return {
            'medical_history_id': self.medical_history_id,
            'prescriptionId': self.prescription_id,
            'medication': self.medication,
            'dosage': self.dosage,
        }

    


    
    
    
