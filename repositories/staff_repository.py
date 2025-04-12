from typing import List, Optional
from models import Staff
from extensions import db
from repositories.interfaces.staff_repository_interface import IStaffRepository

class StaffRepository(IStaffRepository):
    def get_all(self) -> List[Staff]:
        return Staff.query.all()

    def get_by_staff_uuid(self, staff_uuid: str) -> Optional[Staff]:
        return db.session.query(Staff).filter_by(StaffId=staff_uuid).first()

    def add(self, staff: Staff) -> Staff:
        db.session.add(staff)
        db.session.commit()
        return staff

    def update(self, staff: Staff) -> Staff:
        db.session.commit()
        return staff

    def delete(self, staff_id: int) -> None:
        staff = Staff.query.get(staff_id)
        if staff:
            db.session.delete(staff)
            db.session.commit()
