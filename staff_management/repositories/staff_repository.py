from typing import List, Optional
from shared.extensions import db
from staff_management.repositories.interfaces.staff_repository_interface import IStaffRepository
from staff_management.models import Staff
from uuid import UUID
class StaffRepository(IStaffRepository):
    def get_all(self) -> List[Staff]:
        return Staff.query.all()

    def get_by_staff_uuid(self, staff_uuid: UUID) -> Optional[Staff]:
        return db.session.query(Staff).filter_by(id=staff_uuid).first()

    def add(self, staff: Staff) -> Staff:
        
        db.session.add(staff)
        db.session.commit()
        return staff

    def update(self, staff: Staff) -> Staff:
        db.session.commit()
        return staff

    def delete(self, staff_id: UUID) -> None:
        staff = Staff.query.get(staff_id)
        if staff:
            db.session.delete(staff)
            db.session.commit()
        else:
            raise ValueError("Staff member not found")
