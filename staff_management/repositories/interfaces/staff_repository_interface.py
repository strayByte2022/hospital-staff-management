from abc import ABC, abstractmethod
from typing import List, Optional
from staff_management.models import Staff
from uuid import UUID
class IStaffRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Staff]:
        pass

    @abstractmethod
    def get_by_staff_uuid(self, staff_uuid: UUID) -> Optional[Staff]:
        pass

    @abstractmethod
    def add(self, staff: Staff) -> Staff:
        pass

    @abstractmethod
    def update(self, staff: Staff) -> Staff:
        pass

    @abstractmethod
    def delete(self, staff_id: UUID) -> None:
        pass