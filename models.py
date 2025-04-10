from extensions import db
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship

# -----------------------
# Staff model
# -----------------------
class Staff(db.Model):
    __tablename__ = 'staff'

    Id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    StaffId: Mapped[Optional[str]] = mapped_column(db.Text)
    Name: Mapped[Optional[str]] = mapped_column(db.Text)
    Role: Mapped[Optional[str]] = mapped_column(db.Text)
    Speciality: Mapped[Optional[str]] = mapped_column(db.Text)
    Contact: Mapped[Optional[str]] = mapped_column(db.Text)

    doctor = relationship('Doctor', back_populates='staff')


# -----------------------
# Doctor model
# -----------------------
class Doctor(db.Model):
    __tablename__ = 'doctor'

    Id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    StaffId: Mapped[Optional[int]] = mapped_column(db.Integer, db.ForeignKey('staff.Id'))
    LicenseNumber: Mapped[Optional[str]] = mapped_column(db.Text)
    ColumnName: Mapped[Optional[int]] = mapped_column(db.Integer)

    staff = relationship('Staff', back_populates='doctor')


# -----------------------
# Nurse table
# -----------------------
nurse = db.Table(
    'nurse',
    db.metadata,
    db.Column('Id', db.Integer),
    db.Column('StaffId', db.ForeignKey('staff.Id')),
    db.Column('Certification', db.Text)
)


# -----------------------
# Schedule table
# -----------------------
schedule = db.Table(
    'schedule',
    db.metadata,
    db.Column('Id', db.Integer),
    db.Column('StaffId', db.ForeignKey('staff.Id')),
    db.Column('Description', db.Text),
    db.Column('Created', db.Text),
    db.Column('Updated', db.Text)
)


# -----------------------
# Shift table
# -----------------------
shift = db.Table(
    'shift',
    db.metadata,
    db.Column('Id', db.Integer),
    db.Column('StartTime', db.Text),
    db.Column('EndTime', db.Text),
    db.Column('Created', db.Text),
    db.Column('Updated', db.Text),
    db.Column('ScheduleId', db.ForeignKey('schedule.Id'))
)
