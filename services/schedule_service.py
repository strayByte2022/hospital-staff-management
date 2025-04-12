from typing import List, Tuple
from models import Shift
from datetime import date, datetime
from services.interfaces.schedule_service_interface import IScheduleService
from services.interfaces.staff_service_interface import IStaffService
from repositories.interfaces.schedule_repository_interface import IScheduleRepository

class ScheduleService(IScheduleService):
    def __init__(self, schedule_repository: IScheduleRepository, staff_service: IStaffService):
        self.schedule_repository = schedule_repository
        self.staff_service = staff_service
    
    def add_shift(self, staff_id: str, shift_start: datetime, shift_end: datetime) -> Shift:
        if shift_start >= shift_end:
            raise ValueError("Shift start time must be before end time.")
        
        shifts = self.schedule_repository.get_all_shifts(staff_id)
        
        for shift in shifts:
            if (shift.ShiftStart < shift_end and shift.ShiftEnd > shift_start):
                raise ValueError("Shift overlaps with existing shifts.")
            
        shift = Shift(staff_id=staff_id, start_time=shift_start, end_time=shift_end)
        return self.schedule_repository.add_shift(shift)
    
    def get_shifts(self, staff_id: str, range_start: datetime, range_end: datetime) -> List[Shift]:
        shifts = self.schedule_repository.get_all_shifts(staff_id)
        return [shift for shift in shifts if range_start <= shift.ShiftStart <= range_end and range_start <= shift.ShiftEnd <= range_end]
    
    def get_staff_availability(self, staff_id: str, range_start: datetime, range_end: datetime) -> List[Tuple[datetime, datetime]]:
        shifts = self.get_shifts(staff_id, range_start, range_end)
        shifts.sort(key=lambda x: x.start_time)
        availability = []
        for current_shift, next_shift in zip(shifts[:-1], shifts[1:]):
            start_time = max(current_shift.ShiftEnd, range_start)
            end_time = min(next_shift.ShiftStart, range_end)
            
            availability.append((start_time, end_time))
            
        return availability
    
    def get_staff_work_hours(self, staff_id: str, range_start: datetime, range_end: datetime) -> float:
        shifts = self.get_shifts(staff_id, range_start, range_end)
        total_hours = sum((shift.ShiftEnd - shift.ShiftStart).total_seconds() for shift in shifts) / 3600.0
        return total_hours
    
    def remove_shift(self, staff_id: str, shift_id: int) -> None:
        self.schedule_repository.delete_shift(staff_id, shift_id)
    
    def get_available_staff(self, range_start, range_end):
        staff = self.staff_service.list_staff()
        staff_ids = []
        for staff_member in staff:
            shifts = self.get_staff_availability(staff_member.Id, range_start, range_end)
            if len(shifts) > 0:
                staff_ids.append(staff_member.Id)
        
        return staff_ids
    
