from abc import ABC, abstractmethod
from typing import List
from staff_management.models import Shift
from uuid import UUID

class IScheduleRepository(ABC):
    @abstractmethod
    def get_schedule(self,staff_id: UUID) -> List[Shift]:
        pass

    @abstractmethod
    def add_shift(self, staff_id: UUID, shift:Shift) -> Shift:
        pass

    @abstractmethod
    def delete_shift(self, staff_id: UUID, shift_id: int) -> None:
        pass