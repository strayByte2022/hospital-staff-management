from typing import List, Optional

from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Staff(Base):
    __tablename__ = 'staff'

    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(Integer)
    Name: Mapped[Optional[int]] = mapped_column(Integer)
    Role: Mapped[Optional[str]] = mapped_column(Text)
    Speciality: Mapped[Optional[str]] = mapped_column(Text)
    Contact: Mapped[Optional[str]] = mapped_column(Text)

    doctor: Mapped[List['Doctor']] = relationship('Doctor', back_populates='staff')


class Doctor(Base):
    __tablename__ = 'doctor'

    Id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(ForeignKey('staff.Id'))
    LicenseNumber: Mapped[Optional[str]] = mapped_column(Text)
    column_name: Mapped[Optional[int]] = mapped_column(Integer)

    staff: Mapped[Optional['Staff']] = relationship('Staff', back_populates='doctor')


t_nurse = Table(
    'nurse', Base.metadata,
    Column('Id', Integer),
    Column('StaffId', ForeignKey('staff.Id')),
    Column('Certification', Text)
)


t_schedule = Table(
    'schedule', Base.metadata,
    Column('Id', Integer),
    Column('StaffId', ForeignKey('staff.Id')),
    Column('Description', Text),
    Column('Created', Text),
    Column('Updated', Text)
)


t_shift = Table(
    'shift', Base.metadata,
    Column('Id', Integer),
    Column('StartTime', Text),
    Column('EndTime', Text),
    Column('Created', Text),
    Column('Updated', Text),
    Column('ScheduleId', ForeignKey('schedule.Id'))
)
