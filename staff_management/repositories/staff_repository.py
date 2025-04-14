from typing import List, Optional
from shared.extensions import db
from staff_management.repositories.interfaces.staff_repository_interface import IStaffRepository
from staff_management.models import Staff, Nurse, Doctor
from sqlalchemy.orm import with_polymorphic
from uuid import UUID
class StaffRepository(IStaffRepository):
    def get_all(self) -> List[Staff]:
        staff_poly = with_polymorphic(Staff, [Doctor, Nurse])
        results =  db.session.query(staff_poly).all()
        for staff in results:
            print(type(staff))
        return results

    def get_by_staff_uuid(self, staff_uuid: UUID) -> Optional[Staff]:
        staff_poly = with_polymorphic(Staff, [Doctor, Nurse])
    
        return db.session.query(staff_poly).filter(staff_poly.id == staff_uuid).first()

    def add(self, staff: Staff) -> Staff:
        db.session.add(staff)
        db.session.commit()
        return staff

    def update(self, staff: Staff) -> Staff:
        db.session.commit()
        print(type(staff))
        return staff

    def delete(self, staff_id: UUID) -> None:
        staff = db.session.query(Staff).filter(staff_id == staff_id).first()
        
        if staff:
            db.session.delete(staff)
            db.session.commit()
        else:
            raise ValueError("Staff member not found")
