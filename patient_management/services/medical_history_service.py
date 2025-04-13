from patient_management.repositories.interfaces.medical_history_repository_interface import IMedicalHistoryRepository
from typing import List, Optional
from patient_management.models import MedicalHistory, Diagnosis, Allergy, TestResults, Prescription
from patient_management.services.interfaces.medical_history_service_interface import IMedicalHistoryService
from datetime import datetime

class MedicalHistoryService(IMedicalHistoryService):
    def __init__(self, medical_history_repository: IMedicalHistoryRepository):
        self.medical_history_repository = medical_history_repository

    def get_all(self) -> List[MedicalHistory]:
        return self.medical_history_repository.get_all()

    def get_by_patient_id(self, patient_id: str) -> Optional[MedicalHistory]:
        return self.medical_history_repository.get_by_patient_id(patient_id)

    def add(self, patient_id: str) -> MedicalHistory:
        return self.medical_history_repository.add(patient_id)
    
    def add_diagnosis(self, patient_id: str, medical_history_id: int, diagnosis: str) -> None:
        diagnosis = Diagnosis(medical_history_id=medical_history_id, diagnosis=diagnosis)
        self.medical_history_repository.add_diagnosis(patient_id, diagnosis)
        
    def add_allergy(self, patient_id: str, medical_history_id: int, allergy: str) -> None:
        allergy = Allergy(medical_history_id=medical_history_id, allergy=allergy)
        self.medical_history_repository.add_allergy(patient_id, allergy)
        
    def add_test_results(
        self, 
        patient_id: str, 
        medical_history_id: int, 
        date: datetime, 
        result: str
    ) -> None:
        test_results = TestResults(medical_history_id=medical_history_id, date=date, result=result)
        self.medical_history_repository.add_test_results(patient_id, test_results)
        
    def add_prescription(
        self, 
        patient_id: str, 
        medical_history_id: int, 
        medication: str, 
        dosage: str
    ) -> None:
        prescription = Prescription(medical_history_id=medical_history_id, medication=medication, dosage=dosage)
        self.medical_history_repository.add_prescription(patient_id, prescription)