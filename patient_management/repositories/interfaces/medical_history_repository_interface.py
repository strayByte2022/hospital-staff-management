from abc import ABC, abstractmethod
from typing import List, Optional
from patient_management.models import MedicalHistory, Diagnosis, Allergy, TestResults, Prescription
from uuid import UUID

class IMedicalHistoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[MedicalHistory]:
        """Retrieve all medical histories."""
        pass

    @abstractmethod
    def get_by_patient_id(self, patient_id: UUID) -> Optional[MedicalHistory]:
        """Retrieve a medical history by patient ID."""
        pass
    
    @abstractmethod
    def add(self, patient_id: UUID) -> MedicalHistory:
        """Add a new medical history."""
        pass
    
    @abstractmethod
    def add_diagnosis(self,patient_id: UUID, diagnosis: Diagnosis) -> None:
        """Add a diagnosis to a medical history."""
        pass
    
    @abstractmethod
    def add_allergy(self, patient_id: UUID, allergy: Allergy) -> None:
        """Add an allergy to a medical history."""
        pass
    
    @abstractmethod
    def add_test_results(self, patient_id: UUID, test_results: TestResults) -> None:
        """Add test results to a medical history."""
        pass
    
    @abstractmethod
    def add_prescription(self,patient_id: UUID, prescription: Prescription) -> None:
        """Add a prescription to a medical history."""
        pass
    