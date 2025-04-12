from typing import List, Optional
from models import Shift
from extensions import db
from repositories.interfaces.schedule_repository_interface import IScheduleRepository

class ScheduleRepository(IScheduleRepository):
    def get_all_shifts(self,staff_id: str) -> List[Shift]:
        shifts = Shift.query.filter_by(staff_id=staff_id).all()
        return shifts

    def add_shift(self, shift:Shift) -> Shift:
        db.session.add(shift)
        db.session.commit()
        return shift

    def delete_shift(self, staff_id: str, shift_id: int) -> None:
        shift = Shift.query.filter_by(staff_id=staff_id, id=shift_id).first()
        if shift:
            db.session.delete(shift)
            db.session.commit()
