from abc import ABC, abstractmethod
from typing import List
from staff_management.models import Staff
from uuid import UUID

class IStaffService(ABC):
    
    @abstractmethod
    def list_staff(self) -> List[Staff]:
        pass
    
    @abstractmethod
    def get_staff(self, staff_id: UUID) -> Staff:
        pass
    
    @abstractmethod
    def register_staff(self, name: str, role: str, specialty: str, contact: str, license_number: str, certification: str) -> Staff:
        pass
        
    @abstractmethod
    def remove_staff(self, staff_id: UUID) -> None:
        pass
    
    @abstractmethod
    def update_staff(self, staff_id: UUID, name: str, role: str, specialty: str, contact: str) -> Staff:
        pass
    
    
