from abc import ABC, abstractmethod
from typing import List
from models import Shift

class IScheduleRepository(ABC):
    @abstractmethod
    def get_all_shifts(self,staff_id: str) -> List[Shift]:
        pass

    @abstractmethod
    def add_shift(self, shift:Shift) -> Shift:
        pass

    @abstractmethod
    def delete_shift(self, staff_id: str, shift_id: int) -> None:
        pass