from typing import List
from shared.enums import RoleEnum, SpecialityEnum
from staff_management.services.interfaces.staff_service_interface import IStaffService
from staff_management.repositories.interfaces.staff_repository_interface import IStaffRepository
from staff_management.models import Staff, Doctor, Nurse
from uuid import UUID

class StaffService(IStaffService):
    def __init__(self, staff_repository: IStaffRepository): 
        self.staff_repository = staff_repository
        
    def list_staff(self) -> List[Staff]:
        staff_list = self.staff_repository.get_all()
        return staff_list
    
    def get_staff(self, staff_id: UUID) -> Staff:
        staff = self.staff_repository.get_by_staff_uuid(staff_id)
        return staff
    
    def register_staff(self, name: str, role: str, specialty: str, contact: str, license_number: str, certification: str) -> Staff:
        if role not in RoleEnum:
            raise ValueError("Invalid role")
        if specialty not in SpecialityEnum:
            raise ValueError("Invalid specialty")
        
        if role == RoleEnum.DOCTOR:
            staff = Doctor(name=name, role=role, specialty=specialty, contact=contact, license_number=license_number)
        elif role == RoleEnum.NURSE:
            staff = Nurse(name=name, role=role, specialty=specialty, contact=contact, certification=certification)
            
        staff = self.staff_repository.add(staff)
        return staff
        
    def remove_staff(self, staff_id: UUID) -> None:
        self.staff_repository.delete(staff_id)
    
    def update_staff(self, staff_id: UUID, name: str, role: str, specialty: str, contact: str, license_number:str, certification:str) -> Staff:
        if role not in RoleEnum:
            raise ValueError("Invalid role")
        if specialty not in SpecialityEnum:
            raise ValueError("Invalid specialty")
        
        staff = self.staff_repository.get_by_staff_uuid(staff_id)
        if not staff:
            raise ValueError("Staff not found")
        
        staff.name = name
        staff.role = role
        staff.specialty = specialty
        staff.contact = contact
        
        if role == RoleEnum.DOCTOR:
            staff.license_number = license_number
            
        elif role == RoleEnum.NURSE:
            staff.certification = certification
            
        staff = self.staff_repository.update(staff)
        return staff
            
        