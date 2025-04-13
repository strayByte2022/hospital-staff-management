from patient_management.repositories.interfaces.patient_repository_interface import IPatientRepository
from patient_management.models import Patient
from patient_management.services.interfaces.patient_service_interface import IPatientService
from uuid import UUID
class PatientService(IPatientService):
    def __init__(self, patient_repository: IPatientRepository):
        self.patient_repository = patient_repository
        
    def get_all(self):
        return self.patient_repository.get_all()
    
    def get_by_patient_uuid(self, patient_id: UUID) -> Patient:
        return self.patient_repository.get_by_patient_uuid(patient_id)
    
    def add(self, name: str, age: int, gender: str, contact: str, address: str) -> Patient:
        patient = Patient(
            name = name,
            age = age,
            gender = gender,
            contact = contact,
            address = address
        )
        return self.patient_repository.add(patient)

    def update(self, patient_id: UUID, name: str, age: int, gender: str, contact: str, address: str) -> Patient:
        patient = self.patient_repository.get_by_patient_uuid(patient_id)
        if not patient:
            raise ValueError("Patient not found")
        patient.name = name
        patient.age = age
        patient.gender = gender
        patient.contact = contact
        patient.address = address

        return self.patient_repository.update(patient)

    def delete(self, patient_id: UUID) -> None:
        patient = self.patient_repository.get_by_patient_uuid(patient_id)
        if not patient:
            raise ValueError("Patient not found")
        self.patient_repository.delete(patient.id)