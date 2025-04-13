from patient_management.models import MedicalHistory, Allergy, Diagnosis, TestResults, Prescription
from patient_management.repositories.interfaces.medical_history_repository_interface import IMedicalHistoryRepository
from typing import List, Optional
from shared.extensions import db
from uuid import UUID

class MedicalHistoryRepository(IMedicalHistoryRepository):
    def get_all(self) -> List[MedicalHistory]:
        return MedicalHistory.query.all()

   
    def get_by_patient_id(self, patient_id: UUID) -> List[MedicalHistory]:
        return MedicalHistory.query.filter_by(patient_id=patient_id).all()
    
    def add(self, patient_id: UUID) -> MedicalHistory:
        medical_history = MedicalHistory(patient_id=patient_id)
        db.session.add(medical_history)
        db.session.commit()
        return medical_history
    
   
    def add_diagnosis(self, patient_id: UUID, diagnosis: Diagnosis) -> None:
        medical_history: MedicalHistory = MedicalHistory.query.filter_by(patient_id=patient_id, id=diagnosis.medical_history_id).first()
        if medical_history:
            medical_history.diagnosis.append(diagnosis)
            db.session.commit()
        else:
            medical_history = self.add(patient_id)
            medical_history.diagnosis.append(diagnosis)
            db.session.commit()
        
    
   
    def add_allergy(self, patient_id: UUID, allergy: Allergy) -> None:
        medical_history: MedicalHistory = MedicalHistory.query.filter_by(patient_id=patient_id, id=allergy.medical_history_id).first()
        if medical_history:
            medical_history.allergy.append(allergy)
            db.session.commit()
        else:
            medical_history = self.add(patient_id)
            medical_history.allergy.append(allergy)
            db.session.commit()

    
   
    def add_test_results(self, patient_id: UUID, test_results: TestResults) -> None:
        medical_history: MedicalHistory = MedicalHistory.query.filter_by(patient_id=patient_id, id=test_results.medical_history_id).first()
        if medical_history:
            medical_history.test_results.append(test_results)
            db.session.commit()
        else:
            medical_history = self.add(patient_id)
            medical_history.test_results.append(test_results)
            db.session.commit()
    
   
    def add_prescription(self, patient_id: UUID, prescription: Prescription) -> None:
        medical_history: MedicalHistory = MedicalHistory.query.filter_by(patient_id=patient_id, id=prescription.medical_history_id).first()
        if medical_history:
            medical_history.prescription.append(prescription)
            db.session.commit()
        else:
            medical_history = self.add(patient_id)
            medical_history.prescription.append(prescription)
            db.session.commit()