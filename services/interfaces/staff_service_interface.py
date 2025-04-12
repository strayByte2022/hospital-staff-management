from abc import ABC, abstractmethod
from typing import List
from models import Staff

class IStaffService(ABC):
    
    @abstractmethod
    def list_staff(self) -> List[Staff]:
        pass
    
    @abstractmethod
    def get_staff(self, staff_id: str) -> Staff:
        pass
    
    @abstractmethod
    def register_staff(self, name: str, role: str, specialty: str, contact: str) -> Staff:
        pass
        
    @abstractmethod
    def remove_staff(self, staff_id: str) -> None:
        pass
    
    @abstractmethod
    def update_staff(self, staff_id: str, name: str, role: str, specialty: str, contact: str) -> Staff:
        pass
    
    
