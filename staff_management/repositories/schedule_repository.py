from typing import List
from shared.extensions import db
from staff_management.repositories.interfaces.schedule_repository_interface import IScheduleRepository
from staff_management.models import Shift

class ScheduleRepository(IScheduleRepository):
    def get_schedule(self,staff_id: str) -> List[Shift]:
        shifts = Shift.query.filter_by(StaffId=staff_id).all()
        return shifts

    def add_shift(self, shift:Shift) -> Shift:
        
        db.session.add(shift)
        db.session.commit()
        return shift

    def delete_shift(self, staff_id: str, shift_id: int) -> None:
        shift = Shift.query.filter_by(StaffId=staff_id, Id=shift_id).first()
        if shift:
            db.session.delete(shift)
            db.session.commit()
