from abc import ABC, abstractmethod
from typing import List, Optional
from models import Staff

class IStaffService(ABC):
    @abstractmethod
    def list_staff(self) -> List[Staff]:
        pass

    @abstractmethod
    def get_staff(self, staff_id: int) -> Optional[Staff]:
        pass

    @abstractmethod
    def create_staff(self, staff: Staff) -> Staff:
        pass

    @abstractmethod
    def edit_staff(self, staff: Staff) -> Staff:
        pass

    @abstractmethod
    def remove_staff(self, staff_id: int) -> None:
        pass

    @abstractmethod
    def get_staff_by_uuid(self, staff_uuid: str) -> Optional[Staff]:
        pass