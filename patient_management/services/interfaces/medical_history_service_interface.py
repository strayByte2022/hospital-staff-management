from abc import ABC, abstractmethod
from typing import List, Optional
from patient_management.models import MedicalHistory
from datetime import datetime

class IMedicalHistoryService(ABC):
    @abstractmethod
    def get_all(self) -> List[MedicalHistory]:
        """Retrieve all medical histories."""
        pass

    @abstractmethod
    def get_by_patient_id(self, patient_id: str) -> Optional[MedicalHistory]:
        """Retrieve a medical history by patient ID."""
        pass
    
    @abstractmethod
    def add(self, patient_id: str) -> MedicalHistory:
        """Add a new medical history."""
        pass
    
    @abstractmethod
    def add_diagnosis(self, patient_id: str, medical_history_id: int, diagnosis: str) -> None:
        """Add a diagnosis to a medical history."""
        pass
    
    @abstractmethod
    def add_allergy(self, patient_id: str, medical_history_id: int, allergy: str) -> None:
        """Add an allergy to a medical history."""
        pass
    
    @abstractmethod
    def add_test_results(
        self, 
        patient_id: str, 
        medical_history_id: int, 
        date: datetime, 
        result: str
    ) -> None:
        """Add test results to a medical history."""
        pass

    @abstractmethod
    def add_prescription(
        self, 
        patient_id: str, 
        medical_history_id: int, 
        medication: str, 
        dosage: str
    ) -> None:
        """Add a prescription to a medical history."""
        pass