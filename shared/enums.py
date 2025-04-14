# enums.py
from enum import Enum

class RoleEnum(str, Enum):
    NURSE = "Nurse"
    DOCTOR = "Doctor"

class SpecialityEnum(str, Enum):
    GENERAL = "General"
    PEDIATRICS = "Pediatrics"
    CARDIOLOGY = "Cardiology"
    RADIOLOGY = "Radiology"
