from abc import ABC, abstractmethod
from typing import List, Optional
from patient_management.models import Patient
from uuid import UUID

class IPatientService(ABC):
    @abstractmethod
    def get_all(self) -> List[Patient]:
        """Retrieve all patients."""
        pass

    @abstractmethod
    def get_by_patient_uuid(self, patient_id: UUID) -> Optional[Patient]:
        """Retrieve a patient by their UUID."""
        pass

    @abstractmethod
    def add(self, name: str, age: int, gender: str, contact: str, address: str) -> Patient:
        """Add a new patient."""
        pass

    @abstractmethod
    def update(self, patient_id: UUID, name: str, age: int, gender: str, contact: str, address: str) -> Patient:
        """Update an existing patient's information."""
        pass

    @abstractmethod
    def delete(self, patient_id: UUID) -> None:
        """Delete a patient by their ID."""
        pass