from shared.extensions import db
from patient_management.models import Patient
from patient_management.repositories.interfaces.patient_repository_interface import IPatientRepository
from typing import List, Optional
from uuid import UUID

class PatientRepository(IPatientRepository):
    def get_all(self) -> List[Patient]:
        return Patient.query.all()
    
    def get_by_patient_uuid(self, patient_id: UUID) -> Optional[Patient]:
        return Patient.query.filter_by(uuid=patient_id).first()
    
    def add(self, patient: Patient) -> Patient:
        db.session.add(patient)
        db.session.commit()
        return patient
    
    def update(self, patient: Patient) -> Patient:
        db.session.commit()
        return patient
    
    def delete(self, patient_id: UUID) -> None:
        patient = Patient.query.get(patient_id)
        if patient:
            db.session.delete(patient)
            db.session.commit()