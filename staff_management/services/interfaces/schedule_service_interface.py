from abc import ABC, abstractmethod
from typing import List, Tuple
from staff_management.models import Staff, Shift
from datetime import datetime
from uuid import UUID

class IScheduleService(ABC):
    
    @abstractmethod
    def add_shift(self, staff_id: UUID, shift_start: datetime, shift_end: datetime) -> Shift:
        pass
    
    @abstractmethod
    def get_schedule(self, staff_id: UUID, range_start: datetime, range_end: datetime) -> List[Shift]:
        pass
    
    @abstractmethod
    def get_staff_availability(self, staff_id: UUID, range_start: datetime, range_end: datetime) -> List[Tuple[datetime,datetime]]:
        pass
    
    @abstractmethod
    def get_staff_work_hours(self, staff_id: UUID, range_start: datetime, range_end: datetime) -> float:
        pass
    
    @abstractmethod
    def remove_shift(self, staff_id: UUID, shift_id: int) -> None:
        pass
    
    @abstractmethod
    def get_available_staff(self, range_start: datetime, range_end: datetime) -> List[Staff]:
        pass    
    
    
