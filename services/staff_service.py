import uuid
from typing import List, Optional

from enums import RoleEnum, SpecialityEnum
from models import Staff
from services.interfaces.staff_service_interface import IStaffService
from repositories.interfaces.staff_repository_interface import IStaffRepository

class StaffService(IStaffService):
    def __init__(self, staff_repository: IStaffRepository):
        self.staff_repository = staff_repository

    def list_staff(self) -> List[Staff]:
        return self.staff_repository.get_all()

    def get_staff(self, staff_id: int) -> Optional[Staff]:
        return self.staff_repository.get_by_id(staff_id)

    def create_staff(self, staff: Staff) -> Staff:

        staff.StaffId = str(uuid.uuid4())

        if staff.Role not in RoleEnum.value2member_map_:
            raise ValueError(f"Invalid Role: {staff.Role}")

            # Validate Speciality
        if staff.Speciality and staff.Speciality not in SpecialityEnum._value2member_map_:
            raise ValueError(f"Invalid Speciality: {staff.Speciality}")

        return self.staff_repository.add(staff)

    def get_staff_by_uuid(self, staff_uuid: str) -> Optional[Staff]:
        return self.staff_repository.get_by_staff_uuid(staff_uuid)

    def edit_staff(self, staff: Staff) -> Staff:
        return self.staff_repository.update(staff)

    def remove_staff(self, staff_id: int) -> None:
        self.staff_repository.delete(staff_id)
