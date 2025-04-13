# enums.py
from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "Admin"
    NURSE = "Nurse"
    DOCTOR = "Doctor"

class SpecialityEnum(str, Enum):
    GENERAL = "General"
    PEDIATRICS = "Pediatrics"
    CARDIOLOGY = "Cardiology"
    RADIOLOGY = "Radiology"
